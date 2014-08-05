from django.test import TestCase
from encurtador_app.models import *
from encurtador_app.util import *

class UrlTestcase(TestCase):

    " Cria objetos de testes"
    def setUp(self):
        Url.objects.create(url='https://www.youtube.com/')
        Url.objects.create(url='https://www.djangoproject.com')
        Url.objects.create(url='https://www.facebook.com/')

    "Testa se a funcao que gera a url curta busca a url inteira salva no banco de dados"
    def testa_linkar(self):
        slug = 'https://www.exemplo.com/'
        url_nova = Url.objects.create(url=slug)

        url_curta = base62.from_decimal(url_nova.id)

        self.assertEquals(int(url_curta),Url.objects.get(id=base62.to_decimal(url_curta)).id)

    "Testa se o Index possui um campo para inserir a a URL a ser encurtada"
    def testa_index(self):
        resposta = self.client.get('/')
        self.assertEquals(resposta.status_code,200)
        self.assertContains(resposta,'input')

    "Testa se a url inseria no campo e inserida no banco"
    def testa_inserir_url(self):
        qtd_urls = Url.objects.count()
        resposta = self.client.post('/encurtar/',{'url':'https://www.exemplo2.com/'})
        self.assertEquals(resposta.status_code,200)
        self.assertGreater(Url.objects.count(),qtd_urls)

    "testa redirecionamento"
    def testa_redirecionamento(self):
        slug = 'https://www.google.com/'
        url_nova = Url.objects.create(url=slug)

        url_curta = base62.from_decimal(url_nova.id)
        resposta = self.client.get('/'+url_curta)
        self.assertEquals(resposta.url,slug)