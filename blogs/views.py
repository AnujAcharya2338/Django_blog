from django.http import HttpResponse
from django.shortcuts import render

from blogs.models import Blog

# Create your views here.
def post_by_category(request, category_id): 
    posts = Blog.objects.filter(status = 'Published', category = category_id)
    print(posts)
    return HttpResponse(posts)         