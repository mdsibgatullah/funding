from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index.as_view(),name='index'),
    path('about-us',views.AboutUs.as_view(), name="about-us"),
    path('faqs',views.AboutUs.as_view(), name="faqs"),
    path('teams',views.Teams.as_view(), name="teams"),
    path('news',views.News.as_view(), name="news"),
    path('countact-us',views.ContactUs.as_view(), name="countact-us"),
    path('register',views.Register.as_view(), name="register"),
    path('login',views.Login.as_view(), name="login"),
]