from django.shortcuts import render

'''This function is to load landing page.'''


def home(request):
    return render(request, "Plant/landing.html", {})