from django.http import HttpResponse
from django.shortcuts import render

from posts.models import Post


def home(request):
    post =Post.objects.get(id=1)
    return HttpResponse(f"<h1>{post.title}</h1><p>{post.content}</p>")

def post(request):
    post = Post.objects.get(id=1)
    return render(request,template_name="base httml",context={"post":post})


def post_list(request):
    posts = Post.objects.filter(is_published=True, rate__in=range(5, 10))
    return render(request, 'post_list.html', {'posts': posts})




# Create your views here.
