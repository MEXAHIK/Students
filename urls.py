from django.conf.urls.defaults import *
from django.contrib import admin
#from Students.views import views
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('Students.views',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'group_list'),
    (r'^group/$', 'group_list'),
    (r'^group-detail/$', 'group_detail'),
    url(r'^group/(?P<id>\d+)/$', 'group_detail', name = 'group-detail'),
    (r'^student-details/$', 'edit_student'),
    url(r'^student-deurls.pytails/(?P<id>\d+)/$', 'edit_student', name = 'student-details'),
    (r'^group-edit/$', 'edit_group'),
    url(r'^group-edit/(?P<id>\d+)/$', 'edit_group', name = 'group-edit'),
    (r'^add-group/$', 'add_group'),
    (r'^add-student/$', 'add_student'),
    (r'^student-delete/$', 'delete_student'),
    url(r'^student-delete/(?P<id>\d+)/$', 'delete_student', name = 'student-delete'),
    (r'^group-delete/$', 'delete_group'),
    url(r'^group-delete/(?P<id>\d+)/$', 'delete_group', name = 'group-delete'),
    (r'^user/$', 'user_detail'),
    url(r'user/(?P<id>\d+)/$', 'user_detail', name = 'user'),
    (r'logout', 'logout_user'),
    (r'login', 'login_user'),
    (r'autch', 'autch'),
    url(r'^settings/$', 'settings_show'), 
    url(r'^customtags/$',  'custom_tags'),
    )


