from django.urls import path
from .views import upload_image, image_list, process_image, download_image

urlpatterns = [
    path('upload/', upload_image, name='upload_image'),
    path('images/', image_list, name='image_list'),
    path('process/<int:image_id>/', process_image, name='process_image'),
    path('download/<int:image_id>/', download_image, name='download_image'),
]
