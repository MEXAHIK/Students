# -*- coding: UTF-8 -*-
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.shortcuts import get_list_or_404
from studdb.models import Groups
import re

class ClientTest(TestCase):
    """
    Small test suite to demonstrate helper methods.
    You'd probably want to abstract these to your own subclass
    of django.test.TestCase so you could import and use it in
    each of your tests.py files.
    """

    def GET(self, url, status=200, mimetype="text/html"):
        """Get a URL and require a specific status code before proceeding"""
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, status)
        self.failUnless(response.__getitem__('Content-Type').startswith(mimetype))
        return response

    def POST(self, url, params, status=200, mimetype="text/html"):
        """Make a POST and require a specific status code before proceeding"""
        response = self.client.post(url, params)
        self.failUnlessEqual(response.status_code, status)
        self.failUnless(response.__getitem__('Content-Type').startswith(mimetype))
        return response

class SimpleTest(ClientTest):

    fixtures = ['studdb/initial_data.json']

    def test_functions(self):
		
		# проверка на возможность логинится
        login = self.client.login(username='ruslan',
                          password='1')
        self.failUnless(login, 'Could not log in')
        
        # добавление группы
        data_group = {'group_name': 'Abc', 'head_man': ''}
        self.POST('/add-group/', data_group, status=302)
        
        # добавление студента в группу
        group_list = Groups.objects.all()
        group_id = 0
        for g in group_list:
			if g.id > group_id:
				group_id = g.id
        data_student = {'name': 'AAAA',
            'last_name': 'bbbbb',
            'surname':'cccc',
            'birthday': '1987-3-3',
            'nubber_student_ticket': '5555',
            'group': group_id,}
        print group_id
        self.POST('/add-student/', data_student, status=302)
