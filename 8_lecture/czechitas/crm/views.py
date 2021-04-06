from django.http import HttpResponse
from django.views import View


class MujDruhyPohled(View):
    def get(self, request):
        return HttpResponse('Vítej v CRM systému Czechitas!')
