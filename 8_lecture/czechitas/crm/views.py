from django.http import HttpResponse
from django.views import View


class MySecondView(View):
    def get(self, request):
        return HttpResponse(
            '<h1 style="text-align:center">Welcome to Czechitas CRM system!</h1?>'
            '<h3 style="text-align:center"><a href="http://127.0.0.1:8000/courses">Back to courses</a></h1?>'
        )
