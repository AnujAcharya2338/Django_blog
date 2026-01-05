from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def post_by_category(request, category_id): 
    print(category_id)
    return HttpResponse(f"Posts for Category ID")        