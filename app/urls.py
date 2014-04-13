from django.conf.urls import patterns, include, url

from django.contrib import admin
import views

admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyCupola.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login$', views.AtenderPeticiones.login, name='login'),
    url(r'^register$', views.AtenderPeticiones.register, name='register'),
    #url(r'^$', views.AtenderPeticiones.index, name='index'),
    
	)