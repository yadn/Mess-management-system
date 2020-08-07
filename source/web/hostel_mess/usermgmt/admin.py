##import admin modules
from django.contrib import admin

from .models import Student, RebateReq, Meal, OverheadReq	
## Register your models here.
#models being registered
admin.site.register(Student)
admin.site.register(RebateReq)
admin.site.register(Meal)
admin.site.register(OverheadReq)