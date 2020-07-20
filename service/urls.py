from django.urls import path
from . import views

urlpatterns = [
	#沒打任何後綴即會導向預設頁
    path('', views.home_view),
	#所短網址的restful Api
    path('api/shorten-url/', views.url_shortener_api, name='url_shortener_api'),
	#縮短網址URL
    path('l/<slug:slug>/', views.redirector_view),
]