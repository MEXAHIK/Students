from django.contrib import admin
from Students.studdb.models import Groups, Student 

class StudentAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'name', 'surname', 'birthday', 'nubber_student_ticket', 'group')
	
class GroupAdmin(admin.ModelAdmin):
	list_display = ('group_name', 'head_man')

admin.site.register(Student, StudentAdmin)
admin.site.register(Groups, GroupAdmin)
