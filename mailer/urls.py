# Name: Toa Pita
# Section: 003
# Project Description: A short mailer app. First app in django

# Import libraries and my functions
from django.urls import path
from .views import indexPageView,aboutPageView,contactPageView,indexPageRender

# Create path handlers for each of the paths. When the user types a string on the url bar it will call the appropriate function
urlpatterns = [
    path("", indexPageView, name="index"),
    path("about", aboutPageView, name="about"),
    path("contact/<name>/<email>", contactPageView, name="index"),
    path("test", indexPageRender, name="test"),
]
