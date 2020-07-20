from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponseRedirect

#匯入django_rest_framework
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from . import models
from . import serializers

import string
import random


@require_http_methods(['GET',])
def home_view(request):
    # render基本頁面
    return render(request, 'service/home.html')


@require_http_methods(['GET'])
def redirector_view(request, slug):
    # 如果符合就Redirect縮短URL到相對應的URL網址
    try:
		
        service = models.UrlModel.objects.get(slug=slug)
        url = service.url
		
        if not url.startswith('http://') and not url.startswith('https://'):
            url = f'http://{url}'
			
        return HttpResponseRedirect(url)
		
    except Exception as e:
        return HttpResponseRedirect('/')


@api_view(['POST'])
def url_shortener_api(request):
    try:
		#取得使用者url賦予的參數
        users_url = request.data['url']

		#取得縮址過的紀錄並序列化
        domain = request.META['HTTP_HOST']
        service = shorten_url(users_url, domain)
        service_serializer = serializers.ServiceSerializer(service, many=False)
		
        return Response(data={'success': True, 'data': service_serializer.data}, status=status.HTTP_201_CREATED)
		
    except Exception as e:
        return Response(data={'success': False, 'message': f'{str(e)}'}, status=status.HTTP_400_BAD_REQUEST)


def generate_random_string(string_length=6):
	
    #產生亂數字串
    random_string = ''
    alpha_numerals = string.ascii_letters + string.digits
	
    for _ in range(string_length):
        random_string = random_string + random.choice(alpha_numerals)
		
    return random_string


def shorten_url(url, domain):
	
    # 取得亂數字串和驗證資料庫中是否存在
    random_string = generate_random_string()
    service, created = models.UrlModel.objects.get_or_create(slug=random_string)
	
    if created:
        service.url = url
        short_url = f'http://{domain}/l/{random_string}/'
        service.short_url = short_url
        service.save()
        return service
    else:
        shorten_url(url, domain)
