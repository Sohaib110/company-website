from django.shortcuts import render
from app.models import GeneralInfo
# Create your views here.
def index(request):
    

    context={}
    return render(request, 'index.html', context) 
    