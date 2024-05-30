from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Post

# Create your views here.
class PostView(View):
    def get(self,request,id):
        post = Post.objects.get(id=id)

        return render(request,'post.html',{'post':post})
    

@method_decorator(login_required,name='dispatch')
class CreatePostView(View):
    def get(self,request):
        return render(request,'create_post.html')
    
    def post(self,request):
        title = request.POST.get("title")
        content = request.POST.get("content")

        Post.objects.create(title=title,content=content)
        return redirect("/post/create")
    

@method_decorator(login_required,name='dispatch')
class ContactView(View):
    def get(self,request):
        return render(request,'contact.html')