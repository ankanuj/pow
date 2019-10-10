from django.shortcuts import render


def index(request):
	return render(request,'inventors/index.html')

def about(request):
	return render(request,'inventors/about.html')