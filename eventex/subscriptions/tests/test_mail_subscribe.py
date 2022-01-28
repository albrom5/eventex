from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(
            name='Henrique Bastos',
            cpf='12345678901',
            email='henrique@bastos.net',
            phone='11 99612-9950'
        )
        self.resp = self.client.post('/inscricao/', data)
        self.mail = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.mail.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.mail.from_email)

    def test_subscription_email_to(self):
        expect = ['albrom@gmail.com', 'henrique@bastos.net']
        self.assertEqual(expect, self.mail.to)

    def test_subscription_email_body(self):
        contents = [
            'Henrique Bastos',
            '12345678901',
            'henrique@bastos.net',
            '11 99612-9950'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.mail.body)
