from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("hello.. Thanks for stopping by at Index page")
