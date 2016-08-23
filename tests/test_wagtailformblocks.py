"""
test_wagtailformblocks
----------------------------------

Tests for `wagtailformblocks` module.
"""
from __future__ import unicode_literals

import json

from django.test import TestCase
from django.urls import reverse

from wagtailformblocks.models import (BaseForm, EmailForm, FormField,
                                      FormSubmission)


def make_formfields(form):
    FormField.objects.create(
        form=form,
        sort_order=1,
        label="Your email",
        field_type='email',
        required=True,
    )

    FormField.objects.create(
        form=form,
        sort_order=2,
        label="Your message",
        field_type='multiline',
        required=True,
    )

    FormField.objects.create(
        form=form,
        sort_order=3,
        label="Your choices",
        field_type='checkboxes',
        required=False,
        choices='foo,bar,baz',
    )


class TestViews(TestCase):
    def setUp(self):
        self.baseform = BaseForm.objects.create()
        self.emailform = EmailForm.objects.create()
        make_formfields(self.emailform)

    def tearDown(self):
        pass

    def test_process(self):
        url = reverse('wagtailformblocks_process',
                      kwargs={'pk': self.baseform.id})
        data = {}
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 200)

        json_resp = json.loads(resp.content)
        self.assertEqual(json_resp['message'],
                         'Thank you, the form has been submitted.')

    def test_process_form_validation(self):
        url = reverse('wagtailformblocks_process',
                      kwargs={'pk': self.emailform.id})
        data = {}
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 400)

        json_resp = json.loads(resp.content)
        self.assertEqual(json_resp['message'],
                         'There was an error processing the form')

        data = {
            'your-email': 'john@doe.com',
            'your-message': 'This is a test message'
        }
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 200)

    def test_process_form_store_submission(self):
        url = reverse('wagtailformblocks_process',
                      kwargs={'pk': self.emailform.id})
        data = {
            'your-email': 'john@doe.com',
            'your-message': 'This is a test message'
        }
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(FormSubmission.objects.count(), 0)

        self.emailform.store_submission = True
        self.emailform.save()
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(FormSubmission.objects.count(), 1)
