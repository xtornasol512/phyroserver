# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect as redirect301


# Create your views here.
#Dicccionario ejemplo
my_data_dict= {'hola':"fatima"}
meta_keywords = 'PhyroServer, responsive'#key que tendran todas las view

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

#Paginas Base/Secciones
def ecommerce(request):
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

def responsive(request):
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

def marketingOnline(request):
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

def startUp(request):
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

def clientes(request):
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

def contacto(request):
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

def team(request):
    return render_to_response('home/index.html',
                          context_instance=RequestContext(request))

#Paginas de Perfiles
def view_jesus(request):
    ctx={'posts':ultimosPost('xtornasol')}
    return render_to_response('home/index.html', ctx,
                          context_instance=RequestContext(request))

def view_alen(request):
    ctx={'posts':ultimosPost('alen')}
    return render_to_response('home/index.html', ctx,
                          context_instance=RequestContext(request))

def view_luciano(request):
    ctx={'posts':ultimosPost('vash512')}
    return render_to_response('home/index.html', ctx,
                          context_instance=RequestContext(request))

def view_fatima(request):
    ctx={'posts':ultimosPost('fai')}
    return render_to_response('home/index.html', ctx,
                          context_instance=RequestContext(request))

#modulo de obtencion de ultimos post
def ultimosPost(user):
    return ["ultimos post1", "ultimo post2", "ultimo post3"]

"""
=====REDIRECT's RULES===========
"""

#Redireccion de Perfiles
def redi_jesus(request):return redirect301('/team/jesus-alvarado')

def redi_alen(request):return redirect301('/team/alen-lopez')

def redi_luciano(request):return redirect301('/team/luciano-marcos')

def redi_fatima(request):return redirect301('/team/fatima-hernandez')

#Redes Sociales
def twitter(request):
    return redirect301('http://twitter.com/PhyroServer')

def facebook(request):
    return redirect301('https://www.facebook.com/pages/Fenix-Fight-Club-Mexico/215447585145328?fref=ts')

def foursquare(request):
    return redirect('https://es.foursquare.com/v/fenix-fight-club-m%C3%A9xico/4faeb42ee4b0085e227a6b34')
