# -*- coding: utf8 -*-
from django.db import models

class Student(models.Model):
	name = models.CharField('Имя', max_length = 20)
	last_name = models.CharField('Фамилия', max_length = 30)
	surname = models.CharField('Отчество', max_length = 30)
	birthday = models.DateField('Дата рождения')
	nubber_student_ticket = models.IntegerField('Номер зачетной книги', max_length = 20, unique = True)
	group = models.ForeignKey('Groups', verbose_name = 'Группа')
	
	def __unicode__(self):
		return '%s, %s, %s' % (self.last_name, self.name, self.surname)
			
	class Meta:
		ordering = ["group"]

class Groups(models.Model):
	group_name = models.CharField('Группа', max_length = 50)
	head_man = models.ForeignKey(Student, blank = True, null = True, verbose_name = 'Староста')
	
	def __unicode__(self):
		return '%s, %s' % (self.group_name, self.head_man)
	
	class Meta:
		ordering = ["group_name"]
