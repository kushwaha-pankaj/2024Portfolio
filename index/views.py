from django.shortcuts import render
from about.models import About, Testimonial
from index.models import Person, Profile

# Create your views here.
def index(request):
    profile = Profile.objects.first()
    person = Person.objects.first()
    about = About.objects.first()
    testomonials = Testimonial.objects.all()
    context = {
        'profile': profile,
        'person': person,
        'about': about,
        'testomonials': testomonials
    }
    return render(request, 'frontend/index.html', context)