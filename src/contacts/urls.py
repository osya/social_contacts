#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import re_path

from contacts.views import HomeView

app_name = 'contacts'

urlpatterns = [re_path(r'^(?:(?P<backend_name>[\w-]+)/)?$', HomeView.as_view(), name='home')]
