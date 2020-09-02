from django.shortcuts import render
from django.http import HttpResponse
from Account.models import Logins
from .hash import Hash


hash = Hash()

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# the function that used to make new accounts
def sign_up_handler(request):
	# get user name and his password
	user_name = request.GET['user_name']
	user_password = hash.hash_password(str(request.GET['user_password'][0]))
	# create this user in table
	new_user = Logins(user_name=user_name, user_password=user_password)
	return HttpResponse(user_name + str(user_password))