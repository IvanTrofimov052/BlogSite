from django.shortcuts import render
from django.http import HttpResponse
from Account.models import Login
from .hash import Hash


hash = Hash()

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# the function that used to make new accounts
def sign_up_handler(request):
	# get user name and his password
	user_name = request.GET['user_name']
	user_password = hash.hash_password(str(request.GET['user_password']))
	# checked if the user_name is busy 
	if(Login.objects.filter(user_name = user_name)):
		# if name is busy
		return HttpResponse('Name is busy')
	else:
		# if name is not busy
		# create this user in table
		new_user = Login(user_name=user_name, user_password=user_password)
		new_user.save()
		return HttpResponse(user_name + str(user_password))


def sign_in_handler(request):
	# get user name and his password
	user_name = request.GET['user_name']
	user_password = hash.hash_password(str(request.GET['user_password']))
	# checked if we dont have this user name
	if(Login.objects.filter(user_name = user_name)):
		# check the password 
		if(Login.objects.get(user_name = user_name).user_password == user_password):
			# if password is right
			return HttpResponse(user_name + ' ' + user_password)
		else:
			# if password isn't right
			return HttpResponse('not correct password')
	# if we havent this username
	return HttpResponse('this user name in None in our system')