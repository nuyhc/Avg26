from django.urls import path
from image_api.views import ImageAPIView

urlpatterns = [
    path('path/', ImageAPIView.as_view(), name='image-api'),
]