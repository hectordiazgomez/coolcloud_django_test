from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the home page!")

def about(request):
    return HttpResponse("This is the about page.")

def contact(request):
    return HttpResponse("Contact us at example@example.com")

def dynamic_view(request, id):
    return HttpResponse(f"You're viewing item {id}")