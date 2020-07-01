from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from App import classify

# Create your views here.

def index(request):
	return render(request,'index.html')

@csrf_exempt
def classify_image(request):
	image_data = request.POST.get('image_data')
	params = classify.classify_image(image_data)
	return JsonResponse({"Status":params})