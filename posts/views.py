from django.http import HttpResponse
from django.shortcuts import render

from posts.models import Post


def home(request):
    post =Post.objects.get(id=1)
    return HttpResponse(f"<h1>{post.title}</h1><p>{post.content}</p>")

def post(request):
    post = Post.objects.get(id=1)
    return render(request,template_name="base httml",context={"post":post})




# Create your views here.
