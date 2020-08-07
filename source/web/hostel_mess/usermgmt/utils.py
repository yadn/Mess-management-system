##import django modules like auth redirect
#import models as well
from django.contrib.auth.models import User, Group
from django.shortcuts import redirect
from .models import Student, RebateReq, Meal, OverheadReq
## function for checking if manager
# return true if manager
#@param user
def is_manager(user):
	return user.groups.filter(name='manager').exists()


## function for checking if worker
# return true if worker
#@param user
def is_worker(user):
	return user.groups.filter(name='worker').exists()
## function for checking if student
# return true if student
#@param user student
def is_student(user):
	return user.groups.filter(name='student').exists()

##function to generate pending rebate Requests
#return all pending rebate requests
def generate_pending_rebates():
	context = {'pending_rebates':[]}
	for reb in RebateReq.objects.filter(status='W'):
		context["pending_rebates"].extend([{
			'from': str(reb.fromDate),
			'to': str(reb.toDate),
			'ldap':reb.student.user.username,
			'name':f'{reb.student.user.first_name+reb.student.user.last_name}',
			'duration': str((reb.toDate-reb.fromDate).days),
			'id': reb.id
			}])
	if len(context["pending_rebates"])==0:
		return None
	else:
		return context

def generate_pending_overheads():
	context = {'pending_overheads':[]}
	for ovr in OverheadReq.objects.filter(status='W'):
		context["pending_overheads"].extend([{
			'date': str(ovr.date),
			'ldap': ovr.student.user.username,
			'name':f'{ovr.student.user.first_name+ovr.student.user.last_name}',
			'mealType': ovr.mealType,
			'count': ovr.count,
			'id' : ovr.id
			}])
	if len(context["pending_overheads"])==0:
		return None
	else:
		return context

def generate_my_requests(user):
	context = {'prev_overheads':[], 'prev_rebates':[]}
	status = {'W':'HOLD', 'Y':'APPROVED', 'N':'REJECTED'}
	student = Student.objects.filter(user=user)[0]
	for ovr in OverheadReq.objects.filter(student=student):
		context["prev_overheads"].extend([{
			'date': str(ovr.date),
			'meal': ovr.mealType,
			'status': status[ovr.status],
			'count': ovr.count,
			'id' : ovr.id
			}])
	for reb in RebateReq.objects.filter(student=student):
		context["prev_rebates"].extend([{
			'from': str(reb.fromDate),
			'to': str(reb.toDate),
			'status': status[reb.status],
			'id' : reb.id
			}])
	if len(context["prev_overheads"])==0:
		context.pop("prev_overheads")
	elif len(context["prev_rebates"])==0:
		context.pop("prev_rebates")
	return context 
##function to redirect user to it's hamepage
#returns to the homepage
#@param rerequest
def homepage_redirect(request):
	user=request.user
	if is_manager(user):
		return redirect('manager-homepage')
	elif is_worker(user):
		return redirect('worker-homepage')
	else: #is_student(user):
		return redirect('student-homepage')