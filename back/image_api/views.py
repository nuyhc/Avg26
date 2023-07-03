from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from .serializers import ImageSerializer
#from personalcolor.create_background import create_background2
from image_api.create_background import create_background2
import os

from django.core.files.base import ContentFile
from PIL import Image
from django.http import FileResponse
import base64


class ImageAPIView(APIView):
    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.validated_data['image']
            image_path = self.save_image(image)
            create_background2(image_path,"Joy")
            result_path =  "C:/Users/anoth/Desktop/2023capstone/back/reuslt.png"
            #return Response({'result_path' : result_path}, status = status.HTTP_200_OK) 
            return FileResponse(open(result_path, 'rb'), content_type='image/png') #이미지 값 return
            # encoded_image = self.encode_image(result_path)
            # return Response({'encoded_image' : encoded_image}, status = status.HTTP_200_OK) # 이미지 인코딩 후 return 
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def save_image(self, image):
        filename = image.name
        save_path = os.path.join(settings.MEDIA_ROOT, 'images')
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        file_path = os.path.join(save_path, filename)
        with open(file_path, 'wb+') as f:
            for chunk in image.chunks():
                f.write(chunk)
        return file_path
    def encode_image(self, image_path):
        with open(image_path, 'rb') as f:
            image_data = f.read()
        encoded_image = base64.b64encode(image_data).decode('utf-8')
        return encoded_image



