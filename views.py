# -*- coding: UTF-8 -*-

from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from studdb.models import Groups, Student
from django.shortcuts import get_object_or_404, get_list_or_404
from studdb.models import StudentForm, GroupForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import permission_required

def group_list(request):
	groups = Groups.objects.all()
	students = Student.objects.all()
	return render_to_response('group_page.html', {'groups': groups}, context_instance = RequestContext(request))

def group_detail(request, id):
	group  = get_object_or_404(Groups, id = id)
	student_list = group.student_set.all()
	return render_to_response('group_detail.html', {'s_list': student_list, 'group': group}, context_instance = RequestContext(request))

@permission_required('studdb.change_student')
def edit_student(request, id):
	student = get_object_or_404(Student, id = id)
	form = StudentForm(instance = student)
	if request.method == 'POST':
		form = StudentForm(request.POST, instance = student)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/group/')
	return render_to_response('edit_student.html', {'student_details': form}, context_instance = RequestContext(request))

@permission_required('studdb.change_groups')
def edit_group(request, id):
	group = get_object_or_404(Groups, id = id)
	form = GroupForm(instance = group)
	if request.method == 'POST':
		form = GroupForm(request.POST, instance = group)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect ('/group/')
	return render_to_response('edit_group.html', {'form': form}, context_instance = RequestContext(request))

@permission_required('studdb.add_groups')	
def add_group(request):
	form = GroupForm()
	if request.method == 'POST':
		form = GroupForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/group/')
	return render_to_response('add_group.html', {'form': form}, context_instance = RequestContext(request))

@permission_required('studdb.add_student')
def add_student(request):
	form = StudentForm()
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/group/')
	return render_to_response('add_student.html', {'form': form}, context_instance = RequestContext(request))

@permission_required('studdb.delete_student')
def delete_student(request, id):
	show_delete_student = Student.objects.filter(id = id)
	if request.method == 'POST':
		d_student = get_object_or_404(Student, id = id)
		d_student.delete()
		return HttpResponseRedirect('/group/')
	return render_to_response('delete_student.html', {'d_student': show_delete_student}, context_instance = RequestContext(request))

@permission_required('studdb.delete_groups')
def delete_group(request, id):
	d_group = get_object_or_404(Groups, id = id)
	show_delete_group = Groups.objects.filter(id = id)
	show_delete_student = d_group.student_set.all()	
	if request.method == 'POST':		
		d_group.delete()
		return HttpResponseRedirect('/group/')
	return render_to_response('delete_group.html', {'d_group': show_delete_group, 'student_list': show_delete_student}, context_instance = RequestContext(request))

def user_detail(request, id):
	form = get_list_or_404(User, id = id)
	user = get_object_or_404(User, id = id)
#	perm = user.has_perms()
	return render_to_response('user_page.html', {'form': form, 'perm': user}, context_instance = RequestContext(request))

def logout_user(request):
	auth.logout(request)
	return HttpResponseRedirect('/group/')
	
def login_user(request):
	if request.method == "GET":
		username = request.GET.get('username')
		password = request.GET.get('password')
		user = auth.authenticate(username = username, password = password)
		if user is not None and user.is_active:
			auth.login(request, user)
			return HttpResponseRedirect('/group/')
	else:
		return HttpResponseRedirect('/autch/')
	return HttpResponseRedirect('/autch/')

def autch(request):
	return render_to_response ('autch.html')
	
def settings_show(request):
	return render_to_response('settings_show.html', context_instance = RequestContext(request))

def custom_tags(request):
    group = get_object_or_404(Student,  id = 2)
    return render_to_response('custum_tegs.html',  {'group':  group}, context_instance = RequestContext(request))
	
