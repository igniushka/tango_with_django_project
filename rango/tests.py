from django.test import TestCase

def index(request):
    return HttpResponse("Rango says hey there partner!")
