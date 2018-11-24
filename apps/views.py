from django.shortcuts import render, HttpResponse


# Create your views here.
def home(request):
    return render(request, "apps/home.html")


def about(request):
    return render(request, "apps/about.html")


def portfolio(request):
    return render(request, "apps/portfolio.html")


def contact(request):
    return render(request, "apps/contact.html")
