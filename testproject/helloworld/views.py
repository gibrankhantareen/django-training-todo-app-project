from django.http import HttpResponse

def homPageView(request):
	return HttpResponse('Hello World This is my First Program - Gibran')
