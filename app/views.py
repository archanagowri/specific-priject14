from django.shortcuts import render

# Create your views here.

def specific_image(request):
    return render(request,'specific_image.html')