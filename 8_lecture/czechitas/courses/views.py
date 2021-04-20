from django.http import HttpResponse
from django.views import View


class MyFirstView(View):
    def get(self, request):
        return HttpResponse(
            '<h1 style="text-align:center">Welcome to Czechitas website!</h1?>'
            '<h3 style="text-align:center"><a href="http://127.0.0.1:8000/crm">Go to CRM</a></h1?>'
        )
