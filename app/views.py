from django.shortcuts import render
from app.models import GeneralInfo
# Create your views here.
def index(request):
    general_info = GeneralInfo.objects.first()
    
   

    context={
            "company_name":general_info.company_name,
            "location":general_info.location,
            "email":general_info.email,
            "phone":general_info.phone,
            "open_hours":general_info.open_hours,
            "video_url":general_info.video_url,
            "twitter_url":general_info.twitter,
            "facebook_url":general_info.facebook,
            "instagram_url":general_info.instagram,
            "linkedin_url":general_info.linkedin,      
    }
    print(f"context:{context}")
    return render(request, 'index.html', context) 
    