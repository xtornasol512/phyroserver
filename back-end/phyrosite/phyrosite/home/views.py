# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect as redirect301


# Create your views here.
#Dicccionario ejemplo
my_data_dict= {'hola':"fatima"}

"""
=====DIRECTORIO PRINCIPAL===========
"""

def index_view(request):
    
    return render_to_response('home/index.html',
                          my_data_dict,
                          context_instance=RequestContext(request))
#Privacidad
def terminos(request):
    return render_to_response('privacidad/terminosyprivacidad.html',
                          my_data_dict,
                          context_instance=RequestContext(request))

#Paginas Base



"""
=====REDIRECT's RULES===========
"""



#Redes Sociales
def twitter(request):
    return redirect301('http://twitter.com/PhyroServer')

def facebook(request):
    return redirect301('https://www.facebook.com/pages/Fenix-Fight-Club-Mexico/215447585145328?fref=ts')

def youtube(request):
    return redirect('https://www.youtube.com/user/strmrzl')

def foursquare(request):
    return redirect('https://es.foursquare.com/v/fenix-fight-club-m%C3%A9xico/4faeb42ee4b0085e227a6b34')
