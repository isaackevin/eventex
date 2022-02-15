from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Isaac Kevin', cpf='12345678901', email='isaac@kevin.net', phone='79-99960-5104')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]
        
    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'kevin.tecnologia.1@gmail.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['kevin.tecnologia.1@gmail.com', 'isaac@kevin.net']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Isaac Kevin',
            '12345678901',
            'isaac@kevin.net',
            '79-99960-5104'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
