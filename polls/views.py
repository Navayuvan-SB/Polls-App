from django.http import HttpResponse


def index(request):
    return HttpResponse("Hey buddy! Welcome to django!")
