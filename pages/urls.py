from django.urls import path
from .views import HomePageView, AboutPageView, ContactPageView

urlpatterns = [
    path("contact/", ContactPageView.as_view(), name = "contact"), # contact page url
    path("about/", AboutPageView.as_view(), name = "about"), # about page url
    path("", HomePageView.as_view(), name = "home"), # homepageview url
    
]