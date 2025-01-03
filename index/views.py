from django.shortcuts import render
from about.models import About, Testimonial
from blog.models import BlogPost
from index.models import Person, Profile
from portfolio.models import Category, Portfolio
from resume.models import Education, Experience, MyCV, TechnicalSkill, NonTechnicalSkill
from service.models import Service

# Create your views here.
def index(request):
    profile = Profile.objects.first()
    person = Person.objects.first()
    about = About.objects.first()
    testomonials = Testimonial.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    # Get the first 4 technical skills
    first_four_technical_skills = TechnicalSkill.objects.all()[:5]
    # Get the next 4 technical skills
    next_four_technical_skills = TechnicalSkill.objects.all()[5:10]

    # Get the first 4 non-technical skills
    first_four_non_technical_skills = NonTechnicalSkill.objects.all()[:5]
    # Get the next 4 non-technical skills
    next_four_non_technical_skills = NonTechnicalSkill.objects.all()[5:10]
    mycv = MyCV.objects.all()
    services = Service.objects.all()
    portfolio = Portfolio.objects.all()
    category = Category.objects.all()
    print(category)
    blogs = BlogPost.objects.filter(is_published=True).order_by('-publish_date')
    context = {
        'profile': profile,
        'person': person,
        'about': about,
        'testomonials': testomonials,
        'education': education,
        'experience': experience,
        'first_four_technical_skills': first_four_technical_skills,
        'next_four_technical_skills': next_four_technical_skills,
        'first_four_non_technical_skills': first_four_non_technical_skills,
        'next_four_non_technical_skills': next_four_non_technical_skills,
        'mycv': mycv,
        'services': services,
        'portfolio': portfolio,
        'category': category,
        'blogs': blogs
    }
    return render(request, 'frontend/index.html', context)