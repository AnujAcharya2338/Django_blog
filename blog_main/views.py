from django.http import HttpResponse
from django.shortcuts import render

from blogs.models import Blog, Category


def home(request):
    featured_post = Blog.objects.filter(is_featured = True, status = 'Published').order_by('-updated_at')
    post = Blog.objects.filter(is_featured = False, status = 'Published').order_by('-updated_at')
    contex = {
        'featured_posts': featured_post,
        'posts': post,  
    }
    return render(request, 'home.html', contex)  
    