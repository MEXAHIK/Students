from django.template import Library, Node,  Variable

register = Library()

@register.tag
def go_to_admin(parser,  token):
    object = token.split_contents()
    return ShowGroup (object[1])

class ShowGroup (Node):
    def __init__(self,  object):
        self.object = object
    
    def render(self,  context):
        obj = Variable(self.object).resolve(context)
        url = "<a href = /admin/%s/%s/%s/>go edit in admin</a>" % (obj._meta.app_label,  obj._meta.module_name,  obj.id)
        return (url)
    
    
