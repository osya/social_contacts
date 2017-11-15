#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from contacts.views import HomeView, msgraph_authorized

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^msgraph_authorized/$', msgraph_authorized, name='msgraph_authorized')
]
