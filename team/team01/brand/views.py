from django.shortcuts import render

# Create your views here.
def coffee(request):
    return render(request, 'coffee.html')
def chicken(request):
    return render(request, 'chicken.html')
def hair(request):
    return render(request, 'hair.html')
def convenience(request):
    return render(request, 'convenience.html')