from django.http import HttpResponse
from django.views import View


class MySecondView(View):
    def get(self, request):
        return HttpResponse('Welcome to Czechitas CRM system!')
