from django.http import HttpResponse
from django.shortcuts import redirect, render

from blogs.models import Blog, Category 

# Create your views here.
from django.shortcuts import get_object_or_404

def post_by_category(request, category_id): 
    try:
        category = get_object_or_404(Category, pk=category_id)

        posts = Blog.objects.filter(status='Published', category=category)
    except Category.DoesNotExist:
        return render(request, '404.html', status=404)

    # try:
    #     category_id = int(category_id)
    # except ValueError:
    #     return redirect('home')

    # Use get_object_or_404 to handle missing categories safely
    context = {
        'posts': posts,
        'category': category,
    } 
    return render(request, 'post_by_category.html', context)


def blogs(request, slug):
     single_blog = get_object_or_404(Blog, slug=slug, status = 'Published')
     context = {
         'single_blog':single_blog,
     }
     return render(request, 'blogs.html', context)  