from django.shortcuts import render
import pyautogui
import _pickle as pickle
from django.views.decorators import gzip
from django.http.response import StreamingHttpResponse
from PIL import Image
import cv2

from django.http import JsonResponse
from django.http import HttpResponse
import numpy as np
import base64


import base64,json
from io import BytesIO
from PIL import Image
from PIL import Image, ImageOps
from . import forms
def home(request):
    return  render(request,'home.html')
def homes(request):
    try:
        image=pyautogui.screenshot()
        #image=image.resize((1080,700))
        #image=image.resize((10,50))
        image=image.resize((1080,590))#image=image.resize((1080,700))
        #image = ImageOps.flip(image)
        #iarray={'imgarray':image.tobytes()}#(np.array(image, dtype=np.uint8))}
        #print(type(np.array(image, dtype=np.uint8)),type(image))
        #print(base64.b64encode(image))
        img = image
        im_file = BytesIO()
        img.save(im_file, format="JPEG")
        im_bytes = im_file.getvalue()  # im_bytes: image in binary format.
        im_b64 = base64.b64encode(im_bytes)
        iarray={'imgarray':im_b64.decode('utf-8')}
        #return HttpResponse(JsonResponse(iarray))
        #print(iarray)
        return HttpResponse(json.dumps({'picture' : iarray}))
        #return HttpResponse(json.dumps({'picture' : "दिल्ली में स्थगित की राइड सेवाएं"}))
    except:
        print('error')
def home1(request):
    f1=forms.data__f()
    if request.method == "POST":
        f1=forms.data__f(data=request.POST)
        if f1.is_valid():
            print("\nPOST IS VALID\n")
            f1.save()
            return HttpResponse("registered")#redirect("/")
    return  render(request,'html.html',{"f1":f1})
