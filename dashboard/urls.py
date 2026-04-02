from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('categories/', views.categories, name='categories'),
    path('categories/add', views.add_categories, name='add_categories'),
    path('categories/edit/<int:pk>', views.edit_categories, name='edit_categories'),
    path('categories/delete/<int:pk>', views.delete_categories, name='delete_categories'),
    path('post/', views.post, name='post'),
    path('post/add/', views.add_post, name='add_post'),
    path('post/edit/<int:pk>', views.edit_post, name='edit_post'),
    path('post/delete/<int:pk>', views.delete_post, name='delete_post'),
    path('users/', views.users, name='users'),
    path('users/add/', views.add_user, name='add_user'),
    path('users/edit/<int:pk>/', views.edit_user, name='edit_user'),
    path('users/delete/<int:pk>/', views.delete_user, name='delete_user'),

    
]