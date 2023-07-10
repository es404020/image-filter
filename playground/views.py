from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import cv2
import os
from django.conf import  settings
import numpy as np
# Create your views here.


def say_hello(request):
    return  render(request,'hello.html',{'name':'eniola'})

def take(request):

    fileObj=request.FILES['in']

    fs = FileSystemStorage()
    filePathName= fs.save(fileObj.name,fileObj)
    filePathName= fs.url(filePathName)
    sketch= request.POST.get('sketch','off')
    blur= request.POST.get('blur','off')
    sharp = request.POST.get('sharp', 'off')
    native=  request.POST.get('native', 'off')
    params ={"name":"Error is",'string':"Nothing was selected"}

    if(sketch=='on'):
        p=settings.MEDIA_ROOT+filePathName
        jc=cv2.imread(p)
        scale_percent= 0.60
        width = int(jc.shape[1] * scale_percent)
        height = int(jc.shape[0] * scale_percent)
        dim = (width, height)
        resize = cv2.resize(jc, dim, interpolation=cv2.INTER_AREA)
        k = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        sharp = cv2.filter2D(jc, -1, k)
        gray = cv2.cvtColor(jc, cv2.COLOR_BGR2GRAY)
        nat = 255 - gray
        gauss = cv2.GaussianBlur(resize, ksize=(15, 15), sigmaX=0, sigmaY=0)
        def dodgeV2(image,mask):
            return  cv2.divide(image,255-mask,scale=256)
        pencil_jc= gray
        cv2.imwrite(p,pencil_jc)
        params = {'filePathName':filePathName}
        return render(request, 'hello.html',params)









