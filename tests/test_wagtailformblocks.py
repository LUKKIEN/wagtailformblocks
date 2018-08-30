"""
test_wagtailformblocks
----------------------------------

Tests for `wagtailformblocks` module.
"""
from __future__ import unicode_literals

import json

import pytest
from django.urls import reverse

from tests.factory.form import BaseFormFactory, EmailFormFactory
from wagtailformblocks.models import FormField, FormSubmission


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


def get_json(response):
    if hasattr(response, 'json'):  # Django >= 1.9
        return response.json()
    try:
        return json.loads(response.content)
    except TypeError:
        # Happens when response.content is of type bytes (Python 3)
        return json.loads(response.content.decode())


@pytest.mark.django_db
def test_process(client):
    baseform = BaseFormFactory()
    emailform = EmailFormFactory()
    make_formfields(emailform)
    url = reverse('wagtailformblocks_process',
                  kwargs={'pk': baseform.id})
    data = {}
    resp = client.post(url, data)
    assert resp.status_code == 200
    json_resp = get_json(resp)
    assert json_resp['message'] == 'Thank you, the form has been submitted.'


@pytest.mark.django_db
def test_process_form_validation(client):
    emailform = EmailFormFactory()
    make_formfields(emailform)
    url = reverse('wagtailformblocks_process',
                  kwargs={'pk': emailform.id})
    data = {}
    resp = client.post(url, data)
    assert resp.status_code == 400

    json_resp = get_json(resp)
    assert json_resp['message'] == 'There was an error processing the form'

    data = {
        'your-email': 'john@doe.com',
        'your-message': 'This is a test message'
    }
    resp = client.post(url, data)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_process_form_store_submission(client):
    emailform = EmailFormFactory()
    make_formfields(emailform)
    url = reverse('wagtailformblocks_process',
                  kwargs={'pk': emailform.id})
    data = {
        'your-email': 'john@doe.com',
        'your-message': 'This is a test message'
    }
    resp = client.post(url, data)
    assert resp.status_code == 200
    assert FormSubmission.objects.count() == 0

    emailform.store_submission = True
    emailform.save()
    resp = client.post(url, data)
    assert resp.status_code == 200
    assert FormSubmission.objects.count() == 1
