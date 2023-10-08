from django.shortcuts import render,get_object_or_404
from .models import noticepart,notes
from .forms import notesform

from django.http import FileResponse

# Create your views here.
def base(request):
    return render(request,'bitcourse/base.html')
def home(request):
    return render(request, 'bitcourse/home.html')
def notice(request):
    fm=noticepart.objects.all()
    return render (request,'bitcourse/notice.html',{'fm':fm})
def about(request):
    return render(request,'bitcourse/aboutus.html')
def contact(request):
    return render(request,'bitcourse/contactus.html')
def first(request):
    if request.method=='POST':
        fm=notesform(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
           
            fm=notesform()

         
    else:
        fm=notesform()
    note=notes.objects.all()
    return render (request,'bitcourse/first.html',{'fm':fm,'note':note})
def pdfview(request,notes_id):
    pdf=get_object_or_404(notes,pk=notes_id)
    response=FileResponse(pdf.note,content_type='application/pdf')
    return response
def second(request):
    return render(request,'bitcourse/second.html')
def third(request):
    return render(request,'bitcourse/third.html')
