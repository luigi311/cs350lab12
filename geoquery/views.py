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
        
        # The GET query param might be null. Proceed silently to exception clause
        try:
            q = self.request.GET['location'] 
            geolocator = Nominatim()

            # Retrieve Location object for submitted query in form
            loc = geolocator.geocode(q)
            if not loc:
                context['result'] = 'Location not found in Nominatim'
            else:
                # Write location object to template variable. See related template to view how this is displayed.
                context['result'] = loc
        except:
            pass

        return context


class LookupDistanceView(generic.FormView):
    template_name = 'geoquery/lookup_dist.html'
    form_class = LookupForm

    def get_context_data(self, **kwargs):
        context = super(LookupDistanceView, self).get_context_data(**kwargs) 
        
        # The GET query param might be null. Proceed silently to exception clause
        try:
            q = self.request.GET['location'] 
            geolocator = Nominatim()

            # Retrieve Location object for submitted query in form
            loc = geolocator.geocode(q)
            if not loc:
                context['result'] = 'Location not found in Nominatim'
            else:
                # Retrieve Location object for NMHU
                nmhu_loc = geolocator.geocode('1009 diamond st, las vegas, nm')

                # Compute distance between loc and nmhu
                d = distance((loc.latitude, loc.longitude), (nmhu_loc.latitude, nmhu_loc.longitude)).miles

                # Write computed distance to template variable. See related template to view how this is displayed.
                context['result'] = d

        except Exception as e:
            print e
        
        return context





