# -*- coding: utf8 -*-
from django.shortcuts import render,render_to_response,get_object_or_404
from django.template import RequestContext
from django.http import HttpResponsePermanentRedirect

from encurtador_app.forms import *
from encurtador_app.models import *
from encurtador_app.util import *

def index(request):
    """ View para página inicial """

    form_url = UrlForm()

    return render_to_response('index.html', {'form_url':form_url}, RequestContext(request))

def encurtar(request):
    " Grava a URL inserida pelo usuário retornando a url encurtada"
    form_url = UrlForm()
    url_curta = ''

    if request.method == 'POST':
        form_url = UrlForm(request.POST)
        if form_url.is_valid():
            url_field = form_url.cleaned_data['url']

            try:
                url = Url.objects.get(url=url_field)
            except Url.DoesNotExist:
                url = Url(url=url_field)
                url.save()
            "encurta a url com base no ID do objeto gravado"
            url_curta = base62.from_decimal(url.id)

    return render_to_response('index.html', {'form_url':form_url,'url_curta':url_curta}, RequestContext(request))

def linkar(request, link):
    " Busca se a url já foi inserida"
    url = get_object_or_404(Url, id=base62.to_decimal(link))
    url.count += 1
    url.save()
    return HttpResponsePermanentRedirect(url.url)