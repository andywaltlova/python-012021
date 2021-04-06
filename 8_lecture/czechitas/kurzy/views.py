from django.http import HttpResponse
from django.views import View


class MujPrvniPohled(View):
    def get(self, request):
        return HttpResponse('Vítej na webu Czechitas!')
