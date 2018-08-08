from django.http import HttpResponse
from myAuth.models import Account
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer

def user_login(request):
	return render(request, 'login.html')

def get_auth(request):
	return obtain_jwt_token(request)

def create_user_post(request):
	data = request.POST
	user  = Account.objects.create_user(data)
	return HttpResponse(user)

def create_user_get (request):
	return render(request, 'create_user.html')

def create_user(request):
	if request.method == "POST":
		return create_user_post(request)
	else:
		return create_user_get(request)

@permission_classes((IsAuthenticated, ))
def eth_settings(request):
	if request.method == "POST":
		token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
		data = request.POST
		user_data = {'token': token}
		valid_data = VerifyJSONWebTokenSerializer().validate(user_data)
		jwt_user = str(valid_data['user'])
		user = Account.objects.get(email = jwt_user)
		user.eth_token = data["ether_token"]
		user.eth_adress = data["ether_adress"]
		user.save()
		return HttpResponse("OK!")
	else:
		return render(request, 'eth_settings.html')






