from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', LoginView.as_view(template_name='recipes/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/add/', views.recipe_add, name='recipe_add'),
    path('recipe/<int:pk>/edit/', views.recipe_edit, name='recipe_edit'),
    path('recipe/<int:pk>/delete/', views.recipe_delete, name='recipe_delete'),
]