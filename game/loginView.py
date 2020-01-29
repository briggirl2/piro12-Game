import json
import requests
from django.views import View
from django.http import JsonResponse, HttpResponse


class KakaoLoginView(View):
    def get(self, request):
        kakao_access_code = request.GET.get('code', None)
        url = 'https://kauth.kakao.com/oauth/token'
        headers = {
            'Content-type': 'application/x-www-form-urlencoded; charset=utf-8'
        }
        body = {
            'grant_type': 'authorization_code',
            'client_id': '4ab6c9e4504646c05f4a6370251f1cd4',
            'redirect_uri': 'http://localhost:8000',
            'code': kakao_access_code
        }
        kakao_response = requests.post(url, headers=headers, data=body)
        print('aaa')
        print('aaa'+f'{kakao_response.text}')
        return HttpResponse(f'{kakao_response.text}')