#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from contacts.views import HomeView

urlpatterns = [
    url(r'(?:(?P<backend_name>[\w-]+)/)?$', HomeView.as_view(), name='home')
]
