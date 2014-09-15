from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import site.page

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', site.page.index, name='index'),
    url(r'^page', site.page.header, name='header'),
    

)
