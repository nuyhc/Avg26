from django.shortcuts import render, redirect
from .forms import MyForm
from .models import MyModel
#from personalcolor.create_background import create_background2
import os
import json
from django.http import JsonResponse


def upload_image(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            imgmodel= MyModel()
            imgmodel.image = request.POST['image']
            return redirect('upload_image')  
    else:
        form = MyForm()
    return render(request, 'personalcolor/upload.html', {'form': form})

def personal_image(request):
    if request.method == 'POST':
        imgmodel = MyModel()
        imgmodel.image = request.POST['image']
        print(imgmodel.image)
        imgmodel.save()
        folder_path = '"C:/Users/anoth/Desktop/2023capstone/back/media/images"'
        file_list = os.listdir(folder_path)
        sorted_files = sorted(file_list, key=lambda x: os.path.getmtime(os.path.join(folder_path, x)), reverse=True)
        latest_file_path = os.path.join(folder_path, sorted_files[0])
        #create_background2(latest_file_path,"Joy")
        global dic
        dic = {}
        dic['return_image'] == 1

        return JsonResponse(dic)

