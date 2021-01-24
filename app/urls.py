

from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from Home.views import home
from Posts.views import *
from Contact.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor', include('ckeditor_uploader.urls')),
    url(r'^$', home, name='home'),
    url(r'^iletisim/$', contact_view, name ='contact'),
    url(r'^', include('Posts.urls')),

    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
