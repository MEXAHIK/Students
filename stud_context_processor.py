import datetime
from Students import settings

def show_settings(request):
	settings_file = ""
	for lines in open("settings.py"):
		settings_file += "<p>%s</p>" % (unicode(lines, 'UTF-8'))
	
	return {'show_settings': settings_file}
