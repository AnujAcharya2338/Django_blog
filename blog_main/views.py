from django.http import HttpResponse
from django.shortcuts import render

from assignments.models import About
from blogs.models import Blog, Category


def home(request):
    featured_post = Blog.objects.filter(is_featured = True, status = 'Published').order_by('-updated_at')
    post = Blog.objects.filter(is_featured = False, status = 'Published').order_by('-updated_at')

    try:
        about = About.objects.get()
    except:
        about = None

    contex = {
        'featured_posts': featured_post,
        'posts': post,  
        'about': about,  
    }
    return render(request, 'home.html', contex)  
    

