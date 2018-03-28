#coding=utf-8
import os
from django.conf import settings

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


def uploadPic(request):
    return render(request,'booktest/uplodPic.html')

def uploadHandle(request):
    if request.method=='POST':
        pic1= request.FILES['pic1']
        picName= os.path.join(settings.MEDIA_ROOT,pic1.name)
        with open(picName,'w') as pic:
            for c in pic1.chunks():
                pic.write(c)
        return HttpResponse('<img src="/static/media/%s">'%pic1.name)