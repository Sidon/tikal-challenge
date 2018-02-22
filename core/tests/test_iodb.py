from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status

from django.test import TestCase
from core.models import Processo



class ProcesusTestCase(TestCase):

    url = reverse('process-list')
    data = []
    for n in range(5):
        num_proc = str(n + 1) + '0' * 19
        dado_proc = 'Esse é o texto padrão de testes para o processo cujo número inicia com ' + str(n + 1)
        data.append({'numero_proceso': num_proc, 'dados_processo': dado_proc})

    def setup(self):

        self.username = "admin"
        self.email = ""
        self.password = "master.21"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()


    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)


    def test_insert_processo(self):
        for d in data:
            response = self.client.post(self.url, d )
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Processo.objects.count(), 5)

