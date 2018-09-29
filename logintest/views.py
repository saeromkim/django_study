from django.shortcuts import render
from django.http import JsonResponse
from .models import *

def index(request) :
	return render(request, './index.html')

def check_id(request) :
	if request.method == 'GET':
		
		print(request.GET.get('user_id',None))
		user_id=request.GET.get('user_id',None)

		try:
			member_list=Member.objects.get(user_id=user_id)
			result={"result":'true'}
		except:
			result={"result":'false'}

		return JsonResponse(result)

def register_member_db(request) :
	if request.method=='POST' :

		user_id=request.POST['user_id']
		user_pw=request.POST['user_pw']

		new_member=Member(user_id=user_id, user_pw=user_pw)
		new_member.save()

		return render(request, './index.html')


