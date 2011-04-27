from django.conf import settings
from django.conf.urls.defaults import *
from django.views.generic.list import ListView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from books.models import Book

admin.autodiscover()
urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', ListView.as_view(model=Book), {}, 'books'),
)

# Upload URLS
if settings.DEBUG:
    urlpatterns.insert(-2, url(r'^%s(?P<path>.*)' % settings.MEDIA_URL[1:],
        'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))

# Static URLs
urlpatterns += staticfiles_urlpatterns()