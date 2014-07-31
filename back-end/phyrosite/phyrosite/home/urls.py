from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView


urlpatterns=patterns('phyrosite.home.views',
    #HOME
    url(r'^$','index_view', name='vista_principal'),
    #estaticos
    url(r'^humans.txt$', TemplateView.as_view(template_name='home/humans.txt', content_type='text/plain; charset=utf-8')),
    url(r'^robots.txt$', TemplateView.as_view(template_name='home/robots.txt', content_type='text/plain; charset=utf-8')),
    url(r'^sitemap.xml$', TemplateView.as_view(template_name='home/sitemap.xml', content_type='application/xml; charset=utf-8')),
    #Programas
    # url(r'^blog/$', 'blog'), esta url va en la ap de blog
    url(r'^team/$', 'team'),
    url(r'^clientes/$', 'clients'),
    url(r'^hackers-and-devs-tehuacan', 'hack_and_devs'),
    

)