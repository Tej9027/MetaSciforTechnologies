from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to My REST API</h1><p>Go to <a href='/api/'>API</a></p>")
