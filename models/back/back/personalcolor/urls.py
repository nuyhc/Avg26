from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns = [
    path('', views.upload_image, name='upload_image'),
    path('updateimage',views.personal_image, name='updateimage')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)