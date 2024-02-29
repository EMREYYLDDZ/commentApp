from django.shortcuts import render, redirect
from. models import*
from .forms import *
# Create your views here.


def index(request):
    if request.method == 'POST': # Html deki formun methodu post ise:
        form = CommentForm(request.POST) # Methodu post olan formu çek
        if form.is_valid(): #Formdaki alanlar doğru girildiyse
            user_comment = form.save(commit=False) # Kayıt et ama yayınlama
            user_comment.user = request.user 
            user_comment.save()
            form.save() # Formu kaydet
            return redirect('index') # ve ilgili sayfayı tekrar çağır.
        else:
            return render (request,'index.html',context)
        
    comment = Comment.objects.all() # bir modelin içimndeki her value değerini sayfaya göndermek için kullanırız.
    
    tersComment = reversed(comment)
    # for i in tersComment:
    #     print(i)
    
    form = CommentForm()
    context = {
        'yorum':tersComment,
        'form':form,
    }
    return render(request,'index.html',context)


def sil(request):
    if request.method == 'POST': # Formun methodu post ise
        silId = request.POST['silValue'] # Htmldeki inputtan "name" değerini baz alarak id leri çektik.
        silComment= Comment.objects.filter(id = silId) # Filter ile html deki ID ile vertabanında ID eşit olanı al
        silComment.delete()
        return redirect('index')
