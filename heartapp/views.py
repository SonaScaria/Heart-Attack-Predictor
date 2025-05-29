import csv
from .models import hearts
from urllib import request
from django.http import HttpResponse
import joblib
# from django.shortcuts import render, redirect
from django.shortcuts import render
from joblib import load

from heartapp.models import hearts


# model = load('C:/Users/ASUS/heartproject/model.joblib')
# Create your views here.
model = load('C:/Users/ASUS/heartproject/model-joblib')



def index(request):
    return render(request, 'index.html')


def export_to_csv(request):     #export to csv
    heart = hearts.objects.all()
    response = HttpResponse()
    response['Content-Disposition'] = 'attachment; filename=heart.csv'
    writer = csv.writer(response)
    writer.writerow(['age', 'gender', 'cp', 'rbp', 'chl', 'fb', 're', 'hr',
                     'exer', 'olp', 'slp', 'nmv', 'ts'])
    heart_fields = heart.values_list('age', 'gender', 'chp', 'rbp', 'chl', 'fb', 'ecg', 'mhr',
                                     'ex', 'olp', 'sl', 'nm', 'ts')
                                        
    for Heart in heart_fields:
        writer.writerow(Heart)
    return response


def results(request):  # ml deployment
    
    if request.method == "POST":
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        cp = request.POST.get('cp')
        rbp = request.POST.get('rbp')
        cl = request.POST.get('cl')
        fb = request.POST.get('fb')
        ecg = request.POST.get('ecg')
        mhr = request.POST.get('mhr')
        ex = request.POST.get('ex')
        olp = request.POST.get('olp')
        sl = request.POST.get('sl')
        nm = request.POST.get('nm')
        ts = request.POST.get('ts')
        
        ob = hearts()

        y_pred = model.predict([[age, gender, cp, rbp, cl, fb, ecg, mhr, ex, olp, sl, nm, ts]])
                                

        result = y_pred
     
        if (y_pred[0] == 1):
            y_pred = "the patient  has Heart Disease"
        elif (y_pred[0] == 0):
            y_pred = "the patient does not have Heart Disease"
        else:
            y_pred = "some error in processing"

        
        ob.age = age    #database creation
        ob.gender = gender
        ob.chp = cp
        ob.rbp = rbp
        ob.chl = cl
        ob.fb = fb
        ob.ecg = ecg
        ob.mhr = mhr
        ob.ex = ex 
        ob.olp = olp 
        ob.sl = sl
        ob.nm = nm
        ob.ts = ts
        ob.result = result

        ob.save()

        return render(request, 'results.html', {'results': y_pred})
    return render(request, 'index.html')

def details(request):
    return render(request, 'details.html')
 

def risk(request):
    return render(request, 'risk.html')

def export_view(request):
    data = hearts.objects.all()
    return render(request, 'export.html', {'data': data})
