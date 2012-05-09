from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render_to_response


def loginform(request):
	return render_to_response('login.html')

#def login(request):
	#username = request.POST['username']
	#password = request.POST['password']
	#user = authenticate(username = username , password = password)