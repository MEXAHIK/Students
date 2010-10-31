# -*- coding: utf8 -*-
from django.db import models
from django.forms import ModelForm

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
