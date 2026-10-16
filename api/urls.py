from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('services/', views.service_list, name='service-list'),
    path('contact/', views.contact_create, name='contact-create'),
    path('projects/', views.project_list, name='project-list'),
    path('blog/', views.blog_list, name='blog-list'),
    path('blog/<int:pk>/', views.blog_detail, name='blog-detail'),
]