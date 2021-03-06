from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Isaac Kevin', cpf='12345678901', email='isaac@kevin.net', phone='79-99960-5104')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]
        
    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'isaacbasses@outlook.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['isaacbasses@outlook.com', 'isaac@kevin.net']

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
