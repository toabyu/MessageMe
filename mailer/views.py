# Name: Toa Pita
# Section: 003
# Project Description: A short mailer app. First app in django

# Import necessary libraries
from django.shortcuts import HttpResponse, render
from django.urls import path
import random

# Create your views here.

# Index page
def indexPageView(request):
    # Create a list of languages to print on the page
    languages = ["Python","JavaScript","C#","C++","Java","Swift"]
    # Create the output for the page
    output = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title></head><body><center><h1>'
    # Print out a random language twice(purposly two random languages so it usually won't line up)
    output += random.choice(languages) + " is the coolest programming language</h1><h2>Also welcome to ficticious company where we only develop in <u>"+random.choice(languages)+"</u></h2></center></body></html>"
    # Return as a HTTP Response
    return HttpResponse(output)

# About page
def aboutPageView(request):
    # Create the output
    output = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title></head><body><center><h1>'
    # Create random stuff. I ran out of creativity after the last page
    output += "About</h1><br>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</center></body></html>"
    # Return as HTTP Response
    return HttpResponse(output)

# Contact page. Going to be a lot shorter in commenting these functions because they all do about the same thing
def contactPageView(request,name,email):
    # take name and email parameters from the url and print them to the page
    output = name + " we will contact you at "+email
    return HttpResponse(output)

# return the index page on request
def indexPageRender(request):
    return render(request,"mailer/index.html")