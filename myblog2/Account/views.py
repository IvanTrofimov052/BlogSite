from django.shortcuts import render
from django.http import HttpResponse
from Account.models import Logins


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# the function that used to make new accounts
def sign_up_handler(request):
	# get user name and his password
	user_name = request.GET['user_name']
	user_password = request.GET['user_password']
	# create this user in table
	new_user = Logins(user_name=user_name, user_password=user_password)
	return HttpResponse(user_name + user_password)