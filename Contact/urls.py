
from django.conf.urls import url, include
from Contact.views import *


app_name = 'contact'

urlpatterns = [
    url(r'^/iletisim/$', contact_view, name='contact'),
    #url(r'^(?P<id>\d+)/$', about_detail, name='detail'),
]
