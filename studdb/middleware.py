# -*- coding: UTF-8 -*-
import time
from django.db import connection
from django.conf import settings

CONTENT_TYPES = ('text/html', 'application/xhtml+xml')

class QueryTimeMiddlewareShow(object):
	
	def process_request(self, request):
		self._start_time = time.time()
	
	def process_response(self, request, response):
		query_time = time.time() - self._start_time
		numbers_query = len(connection.queries)
		text_request = "Время запросов: %s, количество запросов: %s<br />" % (query_time, numbers_query)
		for i in connection.queries:
			text_request += " запросc: %s<br />" % (i)
		if response.status_code == 200:
			response.content += text_request
		return response
	
