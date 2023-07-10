from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import cv2
import os
from django.conf import  settings
import numpy as np
# Create your views here.

from django.shortcuts import redirect
def say_hello(request):
    return  render(request,'hello.html',{'name':'eniola'})

def take(request):



    fileObj=request.FILES['in']

    if (fileObj):


        fs = FileSystemStorage()
        filePathName= fs.save(fileObj.name,fileObj)
        filePathName= fs.url(filePathName)
        sketch= request.POST.get('sketch','off')
        blur= request.POST.get('blur','off')
        sharp = request.POST.get('sharp', 'off')
        native=  request.POST.get('negative', 'off')
        params ={"name":"Error is",'string':"Nothing was selected"}
        p = settings.MEDIA_ROOT + filePathName
        jc = cv2.imread(p)
        scale_percent = 0.60
        width = int(jc.shape[1] * scale_percent)
        height = int(jc.shape[0] * scale_percent)
        dim = (width, height)
        resize = cv2.resize(jc, dim, interpolation=cv2.INTER_AREA)
        k = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])

        if(sketch=='on'):




            gray = cv2.cvtColor(jc, cv2.COLOR_BGR2GRAY)
            invert_img=cv2.bitwise_not(gray)
            blur_img = cv2.GaussianBlur(invert_img, (111, 111), 0)
            invblur_img = cv2.bitwise_not(blur_img)
            sketch_img = cv2.divide(gray, invblur_img, scale=256.0)
            pencil_jc= sketch_img
            cv2.imwrite(p,pencil_jc)
            params = {'filePathName':filePathName}
            return render(request, 'hello.html',params)

        if (sharp == 'on'):
            sharp = cv2.filter2D(jc, -1, k)
            cv2.imwrite(p, sharp)
            params = {'filePathName': filePathName}
            return render(request, 'hello.html', params)
        if (native == 'on'):
            gray = cv2.cvtColor(jc, cv2.COLOR_BGR2GRAY)
            nat = 255 - gray
            cv2.imwrite(p, nat)
            params = {'filePathName': filePathName}
            return render(request, 'hello.html', params)
        if (blur == 'on'):
            gauss = cv2.GaussianBlur(resize, ksize=(115, 115), sigmaX=0, sigmaY=0)
            cv2.imwrite(p, gauss)
            params = {'filePathName': filePathName}
            return render(request, 'hello.html', params)

    else:
        print('hello')
        return  redirect('playground:home')


def foo() :
    print('jekko')





