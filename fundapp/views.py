from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class Index(TemplateView):
    template_name = "fundapp/index.html"
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context[""] = 
    #     return context
    
class AboutUs(TemplateView):
    template_name = "fundapp/about-us.html"

class Faqs(TemplateView):
    template_name = "fundapp/faqs.html"

class AboutUs(TemplateView):
    template_name = "fundapp/about-us.html"

class Teams(TemplateView):
    template_name = "fundapp/teams.html"

class News(TemplateView):
    template_name = "fundapp/news.html"

class ContactUs(TemplateView):
    template_name = "fundapp/contact-us.html"

class Register(TemplateView):
    template_name = "fundapp/register.html"

class Login(TemplateView):
    template_name = "fundapp/login.html"
    
