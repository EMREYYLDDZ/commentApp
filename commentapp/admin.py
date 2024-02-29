from django.contrib import admin
from .models import *

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    comment = Comment.objects.all() # Bir modelin içindeki her value değerini sayfaya göndermek için kullanılır.
    list_display = ('full_name','email','date')


admin.site.register(Comment,CommentAdmin)