from ast import For, If
from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from joblib import load
# from datetime import datetime
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
from django.http import HttpResponse
from .models import Queries
from django.contrib.auth.models import User
import datetime
import pandas as pd
df=pd.read_csv('C:/Users/Prudence/Desktop/Heart_Disease/Data/framingham (3).csv')

Model = load ('./Model/prediction.joblib')

# Create your views here.
def Homepage(request):
    return render(request,'Hospital/home.html')

def signup(request):
    if request.method == 'POST':

        form=Signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
         form=Signupform()
    dictionary={'form':form}
    return render(request,'Hospital/signup.html',dictionary)
    
def signin(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        form= AuthenticationForm(data=request.POST)
        #authenticate 
        user=authenticate(request,username=username,password=password)
        if form.is_valid():
            login(request,user)
            return redirect('Input')
    else:
        form= AuthenticationForm()
    dictionary={'form':form}
    return render(request,'Hospital/signin.html',dictionary)

def Input(request):
    return render(request,'Hospital/Input.html')

def prediction(request):
    
        gender= request.GET.get('gender')
        if  gender=='Male':
            gender = 1
        else:
            gender = 0
    
        age = request.GET.get('age')  
        
        stroke=request.GET.get('Stroke')
        if  stroke== 'No':
            stroke = 0
        else:
            stroke = 1  
            
        smoke=request.GET.get('Smoker')
        if  smoke== 'No':
            smoke = 0
        else:
            smoke = 1  
        
        hypertension=request.GET.get('Hypertension')
        if  hypertension== 'No':
            hypertension = 0
        else:
            hypertension = 1
            
        cholestrol=request.GET.get('cholestrol')
        
        sys=request.GET.get('systolic_bp')
        
        dia=request.GET.get('diastolic_bp')
            
        diabetes=request.GET.get('diabetes')
        if diabetes == 'No':
            diabetesnum = 0
        else:
            diabetesnum = 1
            
        BMI=request.GET.get('BMI') 
        glucose=request.GET.get('glucose')   

        
        print(gender,age,smoke,stroke,hypertension,diabetesnum,cholestrol,sys,dia,BMI,glucose)
        prediction = Model.predict([[gender,age,smoke,stroke,hypertension,diabetesnum,cholestrol,sys,dia,BMI,glucose]])
        
    
        if prediction==[0]:
            Results=' Not Likely to get Heart Failure in the future'
        else:
            Results='Likely to get Heart Failure in the future'
            
        dictionary={'prediction':Results}
        user= request.user
        Datetime=datetime.datetime.now()
        time=Datetime.strftime('%H:%M')
        date=Datetime.strftime('%Y-%m-%d')
        queries=Queries.objects.create(
            user=user.username,
            date=date,
            time=time,
            result=Results,
        )
        return render(request,'Hospital/prediction.html',dictionary)
  
def report_user(request):
    query=Queries.objects.all()
    template=get_template('Hospital/user_report.html')
    context=template.render({'query':query})
    result=BytesIO()
    pdf=pisa.pisaDocument(BytesIO(context.encode("ISO-8859-1")),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    
def report_graph(request):
    df=pd.read_csv('C:/Users/Prudence/Desktop/Heart_Disease/Data/framingham (3).csv')
    template=get_template('Hospital/report_graph.html')
    context=template.render({"dataset":df.head().to_html(),"datasetdescribe":df.describe().to_html(),"datasetinfo":df.info()})
    result=BytesIO()
    pdf=pisa.pisaDocument(BytesIO(context.encode("ISO-8859-1")),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')