# use to pass information back to view
from django.http import HttpResponse
import datetime
# define function which will receive request and perform task 

def hello(request):
	now = datetime.datetime.now()
	html = "Time {}".format(now)
	return HttpResponse(html)

