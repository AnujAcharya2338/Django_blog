from . import views
from django.urls import include, path
 
urlpatterns = [
    path('<int:category_id>/', views.post_by_category, name='post_by_category'),
]  