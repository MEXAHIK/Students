# -*- coding: UTF-8 -*-

from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from studdb.models import Groups, Student
from django.shortcuts import get_object_or_404, get_list_or_404
from studdb.models import StudentForm, GroupForm

def group_list(request):
	groups = Groups.objects.all()
	students = Student.objects.all()
	return render_to_response('group_page.html', {'groups': groups}, context_instance = RequestContext(request))

def group_detail(request, id):
	group  = get_object_or_404(Groups, id = id)
	student_list = group.student_set.all()
	return render_to_response('group_detail.html', {'s_list': student_list, 'group': group})

def edit_student(request, id):
	student = get_object_or_404(Student, id = id)
	form = StudentForm(instance = student)
	if request.method == 'POST':
		form = StudentForm(request.POST, instance = student)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/group/')
	return render_to_response('edit_student.html', {'student_details': form}, context_instance = RequestContext(request))

def edit_group(request, id):
	group = get_object_or_404(Groups, id = id)
	form = GroupForm(instance = group)
	if request.method == 'POST':
		form = GroupForm(request.POST, instance = group)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect ('/group/')
	return render_to_response('edit_group.html', {'form': form}, context_instance = RequestContext(request))
	
def add_group(request):
	form = GroupForm()
	if request.method == 'POST':
		form = GroupForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/group/')
	return render_to_response('add_group.html', {'form': form}, context_instance = RequestContext(request))

def add_student(request):
	form = StudentForm()
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/group/')
	return render_to_response('add_student.html', {'form': form}, context_instance = RequestContext(request))

def delete_student(request, id):
	show_delete_student = Student.objects.filter(id = id)
	if request.method == 'POST':
		d_student = get_object_or_404(Student, id = id)
		d_student.delete()
		return HttpResponseRedirect('/group/')
	return render_to_response('delete_student.html', {'d_student': show_delete_student}, context_instance = RequestContext(request))

def delete_group(request, id):
	d_group = get_object_or_404(Groups, id = id)
	show_delete_group = Groups.objects.filter(id = id)
	show_delete_student = d_group.student_set.all()	
	if request.method == 'POST':		
		d_group.delete()
		return HttpResponseRedirect('/group/')
	return render_to_response('delete_group.html', {'d_group': show_delete_group, 'student_list': show_delete_student}, context_instance = RequestContext(request))

def test(request):
	return render_to_response('test.html')

