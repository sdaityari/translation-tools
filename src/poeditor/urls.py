from django.conf.urls.defaults import *

urlpatterns = patterns ('poeditor.views',
            (r'^$', 'index'),
            (r'^list/$', 'list'),
            (r'^details/(?P<pofile_id>\w+)/$', 'details'),
)
