from django.urls import path
from . import views

urlpatterns = [
	path('auth/', views.get_auth),
	path('new/', views.create_user),
	path('login/', views.user_login),
	path('eth_settings/', views.eth_settings),
	path('eth/', views.eth),
]