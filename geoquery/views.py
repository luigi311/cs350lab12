# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from geopy.distance import distance  # distance calc with geodisic
from geopy.geocoders import Nominatim # access api to gis db

from .forms import LookupForm

class HomeView(generic.TemplateView):
    template_name = 'geoquery/index.html'


class LookupView(generic.FormView):
    template_name = 'geoquery/lookup.html'
    form_class = LookupForm

    def get_context_data(self, **kwargs):
        context = super(LookupView, self).get_context_data(**kwargs) 
        try:
            q = self.request.GET['location']
        except:
            pass
        
        return context





