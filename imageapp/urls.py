from django.urls import path
from .views import upload_image, image_list, process_image, download_image
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('upload/', upload_image, name='upload_image'),
    path('images/', image_list, name='image_list'),
    path('process/<int:image_id>/', process_image, name='process_image'),
    path('download/<int:image_id>/', download_image, name='download_image'),
]
