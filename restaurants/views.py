from django.shortcuts import render

def hello_world(request):
	context = {
		"msg": "Hello World!",
		}
	return render(request, 'html.html', context)# Create your views here.
