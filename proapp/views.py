from django.shortcuts import render
from django.http import request,JsonResponse
from django.core.files.storage import FileSystemStorage
from random import random
from . models import *

# Create your views here.
def fnprod(req):
    return render(req,'products.html')
def signin(req):
    try:
        if req.method=='POST':
            print("entry")
            mail=req.POST['lmail']
            print(mail)
            lpw=req.POST['lpword']
            print(lpw)
            lobj=tblsignup.objects.get(Email=mail,Password=lpw)
            print("hello muhsin")
            req.session['ses']=lobj.id
            print(req.session['ses'])
            return render(req,'products.html',{'usr':lobj})
    except Exception as e:
        print(e)
    return render(req,'signin.html')
def fnsignup(req):
    try:
        email=req.POST['mail']
        objml=tblsignup.objects.filter(Email=email).exists()
        if objml==False:
            name1=req.POST['name']
            print(name1)
            mbl=req.POST['mobile']
            print(mbl)
            pword1=req.POST['pword']
            print(pword1)
            snupobj=tblsignup(Name=name1,Mobile=mbl,Email=email,Password=pword1)
            snupobj.save()
            return render(req,'products.html',{'msg':'User saved successfully'})
    except Exception as e:
        print(e)
    return render(req,'signup.html',{'msg':'User already exists'})