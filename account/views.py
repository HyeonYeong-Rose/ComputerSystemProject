import json

from .models import Account

from django.views import View
from django.http import JsonResponse,HttpResponse

class SingUpView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            if Account.objects.filter(email = data['email']).exists():
                return HttpResponse(status=400)
            
            
            Account(
                email = data['email'],
                password = data['password']
            ).save()

            return HttpResponse({'message':'회원가입 완료!'}, status=200)

        except KeyError:
            return JsonResponse({'message':'INVALID_KEYS'}, status = 400)


