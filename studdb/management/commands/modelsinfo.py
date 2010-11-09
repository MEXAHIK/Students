# -*- coding: UTF-8 -*-
from django.core.management.base import AppCommand
from django.shortcuts import get_object_or_404

class Command( AppCommand ):
    args = '[studdb]'

    requires_model_validation = True

    def handle_app(self, studdb, **options):
		from studdb.models import Groups, Student
		lines = []
		group = Groups.objects.all()
		for g in group:
			lines.append( "%s id: %s" % (g.group_name, g.id))
			group_obj = get_object_or_404(Groups, id = g.id)
			student = group_obj.student_set.all()
			for s in student:
				lines.append("   %s" % s.name)
		return "\n".join( lines )
