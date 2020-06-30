from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from App import classify

# Create your views here.

def index(request):
	return render(request,'index.html')

def classify_image(request):
    image_data = request.form['image_data']
    params = classify.classify_image(image_data)
    return JsonResponse({"Status":params})