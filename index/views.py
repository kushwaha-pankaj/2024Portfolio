from django.shortcuts import render
from about.models import About, Testimonial
from index.models import Person, Profile
from resume.models import Education, Experience

# Create your views here.
def index(request):
    profile = Profile.objects.first()
    person = Person.objects.first()
    about = About.objects.first()
    testomonials = Testimonial.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    context = {
        'profile': profile,
        'person': person,
        'about': about,
        'testomonials': testomonials,
        'education': education,
        'experience': experience
    }
    return render(request, 'frontend/index.html', context)