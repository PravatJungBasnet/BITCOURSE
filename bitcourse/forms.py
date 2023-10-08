from .models import notes,noticepart
from django import forms
class notesform(forms.ModelForm):
    class Meta:
        model=notes
        fields=['title','note']
class noticeform(forms.ModelForm):
    class Meta:
        model=noticepart
        fields='__all__'
