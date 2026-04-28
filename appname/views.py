# Create your views here.
from django.http import HttpResponse

from posts.models import Post


def home(request):
    post =Post.objects.get(id=1)
    return HttpResponse(f"<h1>")

