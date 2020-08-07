
from django.urls import path
from . import views

#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
## List "urlpatterns" contains all paths and their corresponding views 
urlpatterns = [
	## Default URL redirects to login page
	path('', RedirectView.as_view(url='login/'), name='base'),
	path('login/', views.login_view, name='login'),
	path('logout/', views.logout_view, name='logout'),
	path('homepage/', views.homepage_view, name='homepage'),
	## URL /student/ redirects to students group homepage 
	path('student/', views.student_homepage_view, name='student-homepage'),
	## URL /manager/ redirects to managers' group homepage 
	path('manager/', views.manager_homepage_view, name='manager-homepage'),
	## URL /worker/ redirects to workers' group homepage 
	path('worker/', views.worker_homepage_view, name='worker-homepage'),

	## URL /rebate redirects to Students' rebate requests webpage
	path('rebate/',views.rebate, name='rebate'), 
	## URL /overhead redirects to Students' overhead requests webpage	
	path('overhead/',views.overhead, name='overhead'),
	#this is to be redirected to homepage
	## URL /viewreq/ redirects to Students' requests status webpage
	path('viewreq/',views.viewreq),
	## URL /appreq/ redirects to Workers' webpage for approval of overhead requests
	path('apprreq/',views.apprreq),
	## URL /todaycount/ redirects to Workers' webpage for daily count statistics
	path('todaycount/',views.todaycount),
	## URL /apprebate/ redirects to Mess Manager's webpage for approving rebate requests
	path('apprebate/',views.apprebate),
	## URL /monthlyrepo/ redirects to Mess Manager's webpage for generating monthly report
	path('monthlyrepo/',views.monthlyrepo),
	## URL /dailyreqhist/ redirects to Mess Manager's webpage for viewing daily requests statistics
	path('dailyreqhist/',views.dailyreqhist),

	path('rebate/approve/<int:id>/', views.approve_rebate),
	path('rebate/reject/<int:id>/', views.reject_rebate),

	path('overhead/approve/<int:id>/', views.approve_overhead),
	path('overhead/reject/<int:id>/', views.reject_overhead),
	
]