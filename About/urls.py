from django.conf.urls import url, include
from About.views import *


app_name = 'about'

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', about_detail, name='detail'),
]
