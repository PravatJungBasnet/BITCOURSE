from django.contrib import admin
from .models import noticepart,notes

# Register your models here.
@admin.register(noticepart)
class noticeAdmin(admin.ModelAdmin):
    list_display=['title','image']
@admin.register(notes)
class notesAdmin(admin.ModelAdmin):
    list_display=['title','note']


