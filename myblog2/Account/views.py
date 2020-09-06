from django.shortcuts import render
from django.http import HttpResponse
from Account.models import Login, Session
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
		return HttpResponse('sucsesful')


def sign_in_handler(request):
	# get user name and his password
	user_name = request.GET['user_name']
	user_password = hash.hash_password(str(request.GET['user_password']))
	# checked if we dont have this user name
	if(Login.objects.filter(user_name = user_name)):
		# check the password 
		if(Login.objects.get(user_name = user_name).user_password == user_password):
			# if password is right
			# before make sesion checked is session is busy
			if(Session.objects.filter(session = request.COOKIES["sessionid"])):
				return HttpResponse('Your Session id is busy')
			else:
				# make new session
				new_session = Session(user_name = user_name, session = request.COOKIES["sessionid"])
				new_session.save()
				return HttpResponse('sucsesful')
		# if password isn't right
		return HttpResponse('not correct password')
	# if we havent this username
	return HttpResponse('this user name in None in our system')


def sign_out_handler(request):
	# checked sesion if we doesnt have this session
	if(Session.objects.filter(session = request.COOKIES["sessionid"])):
				# delete this sesion
				Session.objects.get(session = request.COOKIES["sessionid"]).delete()
				return HttpResponse('You exit from account')
	# if we havnt this session
	return HttpResponse('Your Session is not right')


def change_password_handler(request):
	# checked sesion if we doesnt have this session
	if(Session.objects.filter(session = request.COOKIES["sessionid"])):
		# get user name by knowing cookie
		user_name = Session.objects.get(session = request.COOKIES["sessionid"]).user_name
		# get new password
		user_password = hash.hash_password(str(request.GET['user_password']))

		# change the password
		user = Login.objects.get(user_name = user_name)
		user.user_password = user_password
		user.save()
		return HttpResponse('sucsesful')
	# if we havnt this session
	return HttpResponse('Your Session is not right')
