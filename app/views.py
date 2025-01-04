from django.shortcuts import render,redirect
from app.models import( 
                       GeneralInfo,
                       Service,
                       Testimonial,
                       FrequentlyAskedQuestion
)
def index(request):
    general_info = GeneralInfo.objects.first()
    service= Service.objects.all()
    testimonial= Testimonial.objects.all()
    faqs= FrequentlyAskedQuestion.objects.all()
    
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
            
            "services":service, 
            
            "testimonials":testimonial,
            "faqs":faqs
            
            
                
    }
    print(f"context:{context}")
    return render(request, 'index.html', context) 


def contact_form(request):
        if request.method == 'POST':
            print("\n user has submitted the contact form")
            print(f" request.POST: {request.POST}")
            name=request.POST.get('name')
            email=request.POST.get('email')
            subject=request.POST.get('subject')
            message=request.POST.get('message')
            
            print(f"name: {name}")
            print(f"email: {email}")
            print(f"subject: {subject}")
            print(f"message: {message}")
        return redirect('home')

    