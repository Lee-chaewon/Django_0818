from django.shortcuts import render
from .models import Portfolio

def portfolio(request):
    return render(request, 'portfolio/portfolio.html')




def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio/portfolio.html', {'portfolios': portfolios})