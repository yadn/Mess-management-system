## import django modules for databases
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


##Student table creation class
#attributes - name, card no. etc.
class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	cardNo = models.CharField(max_length=4, blank=True)
	phoneNo = models.IntegerField(blank=True)
	foodType = models.CharField(max_length = 2, choices = [('v','veg'),('nv','nonveg'),('j','jain')], default = 'v')
	roomNo = models.IntegerField()

	def __str__(self):
		return self.user.username

##Class for ReRebateReq table creation
#attributes - student, date etc.
class RebateReq(models.Model):
	student = models.ForeignKey(Student,on_delete=models.CASCADE)

	fromDate = models.DateField(max_length=10, help_text="format : DDMMYYYY", null=True)
	toDate = models.DateField(max_length=10, help_text="format : DDMMYYYY", null=True)
	status = models.CharField(max_length = 1, choices = [('Y','yes'),('N','no'), ('W','wait')])

	def __str__(self):
		return f'{self.student.user.username}({self.fromDate}-{self.toDate})'
##Class for Meal table creation
#attributes - mealType, price.
class Meal(models.Model):
	mealType = models.CharField(max_length=1, choices=[('B','breakfast'),('L','lunch'),('S','snacks'),('D','dinner')], primary_key=True)
	price = models.IntegerField(default = 60)

	def __str__(self):
		return self.mealType
##Class for ReRebateReq table creation
#attributes - student,mealType, date etc.
class OverheadReq(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	mealType = models.ForeignKey(Meal,on_delete=models.CASCADE)

	date = models.DateField(max_length=10, help_text="format : DDMMYYYY", null=True, auto_now_add=True)
	status = models.CharField(max_length = 1, choices = [('Y','yes'),('N','no'), ('W','wait')])
	count = models.IntegerField(default = 1)

	def __str__(self):
		return f'{self.student.user.username}({self.date}-{self.count})'