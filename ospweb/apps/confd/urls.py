# _*_ coding: utf-8 _*_

from django.conf.urls import url,include
from .views import *

urlpatterns = [
    url(r'^project', include([
        url(r'^list/$', ProjectListView.as_view(), name="project_list"),
        url(r'^add/$', CreateProjectView.as_view(), name="create_project"),

    ])),

    url(r'^vhost', include([
        url(r'^list/$', VhostListView.as_view(), name="vhost_list"),
        url(r'^add/$', CreateVhostView.as_view(), name="create_vhost"),
        url('^detail/(?P<pk>[0-9]+)/$', VhostDetailView.as_view(), name='detail_vhost'),

    ])),


]
