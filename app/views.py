from django.shortcuts import render
from app.models import GeneralInfo

# Create your views here.
def index(request):
    
    
    
    
    all_records = GeneralInfo.objects.all()
    print(all_records)
    
    
    
    
    
    
    
    context={}
    return render(request, 'index.html', context) 
    