from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'clients.views.index'),
	url(r'^companies/$','clients.views.list_companies'),
	url(r'^users/$', 'clients.views.users'),
	url(r'^about/$', 'clients.views.about'),
    	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    	url(r'^admin/', include(admin.site.urls)),
	url(r'^media/(?P<path>.*)$','django.views.static.serve',
		{'document_root':settings.MEDIA_ROOT,}
	),
	url(r'^company/(?P<id_company>\d+)$','clients.views.companies_details'),
	url(r'^contact/$','clients.views.contact'),
	url(r'^company/new/$','clients.views.new_company'),
	url(r'^comment/$','clients.views.new_comment'),
	url(r'^user/new/$','clients.views.new_user'),
	url(r'^signin/$','clients.views.signin'),
	url(r'^private/$','clients.views.private'),
	url(r'^close/$', 'clients.views.close'),
)