from django.shortcuts import render
import requests
from django.http import HttpResponse
import re
import json
import datetime
from myAuth.models import Account
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer

@permission_classes((IsAuthenticated, ))
def get_ether(request):
	token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
	user_data = {'token': token}
	valid_data = VerifyJSONWebTokenSerializer().validate(user_data)
	jwt_user = str(valid_data['user'])
	user = Account.objects.get(email = jwt_user)
	key = user.eth_token
	adress = user.eth_adress

	url = f"https://api.etherscan.io/api?module=stats&action=ethprice&apikey={key}"
	response = requests.get(url)
	eth_rate = re.search(r'(?<="ethusd":")\d*\.\d*', response.text).group(0)

	url = f"https://api.etherscan.io/api?module=proxy&action=eth_blockNumber&apikey={key}"
	response = requests.get(url)
	last_block_num = re.search(r'(?<="result":")[^"]*', response.text).group(0)

	url = f"http://api.etherscan.io/api?module=account&action=balance&address={adress}&tag=latest&apikey={key}"
	balance = requests.get(url).json()["result"]

	url = f"http://api.etherscan.io/api?module=proxy&action=eth_getBlockByNumber&tag={last_block_num}&boolean=true&apikey={key}"
	response = requests.get(url).json()["result"]

	number = int(response["number"], 16) 
	date = datetime.datetime.fromtimestamp(int(response["timestamp"], 16))
	date = f"{date.day}.{date.month}.{date.year}\n{date.hour}:{date.minute}:{date.second} +UTC"
	block_hash = response["hash"]
	gasUsed = int(response["gasUsed"], 16)
	difficulty = int(response["difficulty"], 16)
	link = f"https://etherscan.io/block/{number}"

	data = {"eth_rate":eth_rate,
			"number":number, 
			"date":date, 
			"block_hash":block_hash, 
			"gasUsed":gasUsed, 
			"difficulty":difficulty,
			"balance":balance,
			"link":link}

	return render(request, 'eth_data.html', data)
