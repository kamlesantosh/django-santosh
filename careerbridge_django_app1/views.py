from django.http import HttpResponse
from django.shortcuts import  render
from django.http import HttpResponse
from .models import Student


#create your views here....
def home(request):
    return HttpResponse("welcome To Django Training At CareerBridge!")

def index(request):
    our_dict = {"insert_CareerBridge":"career Bridge  Coming from careerbridge_django_app1/index.html !"}
    return render(request,'careerbridge_django_app1/index.html',context=our_dict)

def Student_table(request):
    Students = Student.objects.all()
    return render(request, 'careerbridge_django_app1/Student_table.html',{'Student':Students})








