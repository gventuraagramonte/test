from django.shortcuts import render

# Create your views here.
def list_portfolio(request):
    return render(request, 'index.html')