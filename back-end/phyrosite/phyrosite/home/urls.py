from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

urlpatterns=patterns('phyrosite.home.views',
    #HOME
    url(r'^$','index_view', name='vista_principal'),
    #estaticos
    url(r'^humans.txt$', TemplateView.as_view(template_name='home/humans.txt', content_type='text/plain; charset=utf-8')),
    url(r'^robots.txt$', TemplateView.as_view(template_name='home/robots.txt', content_type='text/plain; charset=utf-8')),
    url(r'^sitemap.xml$', TemplateView.as_view(template_name='home/sitemap.xml', content_type='application/xml; charset=utf-8')),
    #secciones
    url(r'^ecommerce/$', 'ecommerce'),
    url(r'^responsive/$', 'responsive'),
    url(r'^marketing-online/$', 'marketingOnline'),
    url(r'^startUp/$', 'startUp'),
    url(r'^clientes/$', 'clientes'),
    url(r'^contacto/$', 'contacto'),
    url(r'^team/$', 'team'),
    #chuko y sus variantes
    url(r'^team/jesus-alvarado/$', 'view_jesus'),#principal
    url(r'^yisus/$', 'redi_jesus'),
    url(r'^xtornasol/$', 'redi_jesus'),
    url(r'^garzon/$', 'redi_jesus'),
    url(r'^chuchin/$', 'redi_jesus'),
    url(r'^cxu/$', 'redi_jesus'),
    url(r'^cxuko/$', 'redi_jesus'),
    url(r'^jesus/$', 'redi_jesus'),
    url(r'^chuko/$', 'redi_jesus'),
    url(r'^chucho/$', 'redi_jesus'),
    url(r'^xtornasol512/$', 'redi_jesus'),
    #alen y sus variantes
    url(r'^team/alen-lopez/$', 'view_alen'),
    url(r'^team/alen/$', 'redi_alen'),
    url(r'^alen/$', 'redi_alen'),
    #chano y sus variantes
    url(r'^team/luciano-marcos/$', 'view_luciano'),
    url(r'^team/luciano/$', 'redi_luciano'),
    url(r'^team/vash/$', 'redi_luciano'),
    url(r'^team/vash512/$', 'redi_luciano'),
    url(r'^luciano/$', 'redi_luciano'),
    url(r'^vash/$', 'redi_luciano'),
    url(r'^vash512/$', 'redi_luciano'),
    #fatima y sus variantes
    url(r'^team/fatima-hernadez/$', 'view_fatima'),

    #Programas
    # url(r'^blog/$', 'blog'), esta url va en la ap de blog
    #url(r'^team/$', 'team'),
    #url(r'^clientes/$', 'clients'),
    #url(r'^hackers-and-devs-tehuacan', 'hack_and_devs'),

)