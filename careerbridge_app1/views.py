from django.shortcuts import HttpResponse, render

# Create your views here.
#def home(request)
# return HttpResponse("welcome to Django Training At Careerbridge!")

def index(request):
    our_dict = {'insert_Careerbridge':"Career Bridge Django Training coming From careerbridge_django_app1/inedx.html "}
    return render(request,'careerbridge_django_app1/index.html',context=our_dict)