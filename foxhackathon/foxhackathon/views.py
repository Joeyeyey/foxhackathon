from django.http import HttpResponse

def index(request):
    with open("index.html", "r") as f:
        html = str(f.read())
        return HttpResponse(html)
