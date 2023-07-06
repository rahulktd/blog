from django.http import HttpResponse
from django.shortcuts import render

from core.models import Post


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request,'Modified_files/front.html', {'posts': posts})


