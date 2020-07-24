from django.http import HttpResponse

def home(request):
	res = HttpResponse()
	res.content = "<h1>Hello world</h1>"  	
	return res
