from django.views import View
from django.http import HttpResponse

class HelloWorldView(View):
    def get(self, request):
        html = "<html><body><h1>Hello, World!</h1></body></html>"
        return HttpResponse(html)