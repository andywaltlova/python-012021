from django.http import HttpResponse
from django.views import View


class MyFirstView(View):
    def get(self, request):
        return HttpResponse('Welcome to Czechitas websites!')
