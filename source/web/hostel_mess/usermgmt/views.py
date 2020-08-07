##import django modules for rendering and redirecting
#import django modules for http 
#import django modules for authentication
#import django modulesdecorators
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from usermgmt.utils import *
from .models import Student, RebateReq, Meal, OverheadReq


##Creating imp. views show users
# Create your views here.
@login_required
def homepage_view(request):
	##get the user object and send in context
	return homepage_redirect(request)
##view function for login page of the site
def login_view(request):
	"""View function for login page of site"""
	if request.method == 'GET':
		##check if user is authenticated
		if request.user.is_authenticated:
			return redirect('homepage')
			## return render(request, 'viewreq.html', context=None)
		else:
			return render(request, 'login.html')

	elif request.method == 'POST':
		## return HttpResponse('<p> Great! logged in!</p>')
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		valuenext= request.POST.get('next')

		if user is not None:
			login(request, user)
			if valuenext=="":
				return redirect('homepage')
			else:
				return redirect(valuenext)
		else:
			return render(request, 'login.html', context={'error_msg':'Invalid Username/Password.'})
			## return render(request, 'viewreq.html', context=None)

## function for view after logout
#return if successfully logged out or not
#@param request
def logout_view(request):
	if request.user.is_authenticated:
		logout(request)
		return HttpResponse('<p> Successfully logged out! Please refresh to go to main page.</p>')
	else:
		return redirect('base')
##Showing homepage of student 
#checking if student or not
#@param request
@login_required
@user_passes_test(is_student)
def student_homepage_view(request):
	context = generate_my_requests(request.user)
	return render(request, 'viewreq.html', context=context)

##Showing homepage of manager 
#checking if manager or not
#@param request
@login_required
@user_passes_test(is_manager)
def manager_homepage_view(request):
	context = generate_pending_rebates()
	return render(request, 'apprebate.html', context=context)

##Showing homepage of worker
#checking if worker or not
#@param request
@login_required
@user_passes_test(is_worker)
def worker_homepage_view(request):
	context = generate_pending_overheads()
	return render(request, 'appreq.html', context=context)


##functions to show rebates page
#@param request
@login_required
def rebate(request):
	student = Student.objects.filter(user=request.user)[0]
	reb = RebateReq()
	if request.method == 'GET':
		return render(request, 'rebates.html')
	elif request.method == 'POST':
		fromDate = request.POST['from']
		toDate = request.POST['to']
		reb.student = student
		reb.fromDate = fromDate
		reb.toDate = toDate
		reb.status = 'W'
		reb.save()
		return redirect('homepage')

##functions to show rebates page
#@param request
@login_required
def overhead(request):
	student = Student.objects.filter(user=request.user)[0]
	ovr = OverheadReq()
	if request.method == 'GET':
		return render(request, 'overheads.html')
	elif request.method == 'POST':
		ovr.student = student
		ovr.mealType = Meal.objects.get(mealType=request.POST['mealType'])
		# ovr.date = request.POST['date']
		ovr.count = request.POST['count']
		ovr.status = 'W'
		ovr.save()
		return redirect('homepage')		

@login_required
@user_passes_test(is_manager)
def approve_rebate(request,id):
	reb = RebateReq.objects.get(id=id)
	reb.status='Y'
	reb.save()
	return redirect('manager-homepage')


@login_required
@user_passes_test(is_manager)
def reject_rebate(request,id):
	reb = RebateReq.objects.get(id=id)
	reb.status='N'
	reb.save()
	return redirect('manager-homepage')

@login_required
@user_passes_test(is_worker)
def approve_overhead(request,id):
	reb = OverheadReq.objects.get(id=id)
	reb.status='Y'
	reb.save()
	return redirect('worker-homepage')


@login_required
@user_passes_test(is_worker)
def reject_overhead(request,id):
	reb = OverheadReq.objects.get(id=id)
	reb.status='N'
	reb.save()
	return redirect('worker-homepage')


##functions to show view request page
#@param request
def viewreq(request):
	return render(request, 'viewreq.html')

##functions to show approve request page
#@param request
def apprreq(request):
	return render(request, 'apprreq.html')

##functions to show today count page
#@param request
def todaycount(request):
	return render(request, 'todaycount.html')


##functions to show approve rebate page
#@param request
def apprebate(request):
	return render(request, 'apprebate.html')

##functions to show monthlyrepo page
#@param request
def monthlyrepo(request):
	return render(request, 'monthlyrepo.html')

##functions to show daily request page
#@param request
def dailyreqhist(request):
	return render(request, 'dialyreqhist.html')
