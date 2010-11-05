# -*- coding: utf8 -*-
from django.db import models
from django.forms import ModelForm
from django.db.models.signals import pre_save, pre_delete, post_save
import datetime

class Student(models.Model):
	name = models.CharField('Имя', max_length = 20)
	last_name = models.CharField('Фамилия', max_length = 30)
	surname = models.CharField('Отчество', max_length = 30)
	birthday = models.DateField(verbose_name = 'Дата рождения')
	nubber_student_ticket = models.IntegerField('Номер зачетной книги', max_length = 20, unique = True)
	group = models.ForeignKey('Groups', verbose_name = 'Группа')
	
	def __unicode__(self):
		return '%s, %s, %s, %s, %s' % (self.last_name, self.name, self.surname, self.birthday, self.nubber_student_ticket)
			
class Groups(models.Model):
	group_name = models.CharField('Группа', max_length = 50)
	head_man = models.ForeignKey(Student, blank = True, null = True, verbose_name = 'Староста')
	
	def __unicode__(self):
		return '%s' % (self.group_name)
	
	class Meta:
		ordering = ["group_name"]

class StudentForm(ModelForm):
	class Meta:
	    model = Student
	    fields = ['name', 'last_name', 'surname', 'birthday', 'nubber_student_ticket', 'group']

class GroupForm(ModelForm):
	class Meta:
		model = Groups
		fields = ['group_name', 'head_man']

class Report(models.Model):
	name_model = models.CharField(max_length = 10)
	what_made = models.CharField(max_length = 15)
	text = models.CharField(max_length = 200, blank = True, null = True)
	date_change = models.DateField()
	def __unicode__(self):
		return "%s %s" % (self.name_model, self.what_made)

def handler_delete(sender, **kwargs):
	object_d = kwargs.get('instance')
	if object_d._meta.module_name != 'report':
		name_model = object_d._meta.module_name
		what_made = "Delete"
		date_change = datetime.datetime.now()
		test = "%s %s, %s" % (what_made, name_model, date_change)
		print test
		report_temp = Report(name_model = name_model, what_made = what_made, date_change = date_change)
		report_temp.save()

def handler_change(sender, created, **kwargs):
	object_ch = kwargs.get('instance')
	if object_ch._meta.module_name != 'report':
		object_c = kwargs.get('instance')
		name_model = object_c._meta.module_name	
		date_change = datetime.datetime.now()
		if not created:
			what_made = "Change"
		else:
			what_made = "Addad"
		print "%s %s, %s" % (what_made, name_model, date_change)
		report_temp = Report(name_model = name_model, what_made = what_made,date_change = date_change)
		report_temp.save()
	
pre_delete.connect(handler_delete)
post_save.connect(handler_change)

