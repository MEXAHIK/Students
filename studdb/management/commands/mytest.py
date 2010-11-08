from django.core.management.base import AppCommand
from optparse import make_option

class Command( AppCommand ):
    option_list = AppCommand.option_list + (
        make_option('--count', action='store_true', dest='count', default= False,
            help='Add object count information' ),
    )
    help = 'Prints model names for given application and optional object count.'
    args = '[studdb]'

    requires_model_validation = True

    def handle_app(self, studdb, **options):
        from django.db.models import get_models

        lines = []

        for model in get_models( studdb ):
            lines.append( "[%s]" % model.__name__ )

        return join( lines )
