from django.http import HttpResponse
from django.shortcuts import redirect, render

from blogs.models import Blog, Category 

# Create your views here.
from django.shortcuts import get_object_or_404

def post_by_category(request, category_id): 

    try:
        category_id = int(category_id)
    except ValueError:
        return redirect('home')

    # Use get_object_or_404 to handle missing categories safely
    category = get_object_or_404(Category, pk=category_id)

    posts = Blog.objects.filter(status='Published', category=category)
    
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'post_by_category.html', context)