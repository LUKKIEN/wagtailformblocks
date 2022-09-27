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


@pytest.mark.django_db
def test_process(client):
    baseform = BaseFormFactory()
    emailform = EmailFormFactory()
    make_formfields(emailform)
    url = reverse('wagtailformblocks_process', kwargs={'pk': baseform.id})
    data = {}
    resp = client.post(url, data)
    assert resp.status_code == 200
    assert resp.json()['message'] == 'Thank you, the form has been submitted.'


@pytest.mark.django_db
def test_process_form_validation(client):
    emailform = EmailFormFactory()
    make_formfields(emailform)
    url = reverse('wagtailformblocks_process', kwargs={'pk': emailform.id})
    data = {}
    resp = client.post(url, data)
    assert resp.status_code == 400
    assert resp.json()['message'] == 'There was an error processing the form'

    data = {
        'your_email': 'john@doe.com',
        'your_message': 'This is a test message'
    }
    resp = client.post(url, data)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_process_form_store_submission(client):
    emailform = EmailFormFactory()
    make_formfields(emailform)
    url = reverse('wagtailformblocks_process', kwargs={'pk': emailform.id})
    data = {
        'your_email': 'john@doe.com',
        'your_message': 'This is a test message'
    }
    resp = client.post(url, data)
    assert resp.status_code == 200
    assert FormSubmission.objects.count() == 0

    emailform.store_submission = True
    emailform.save()
    resp = client.post(url, data)
    assert resp.status_code == 200
    assert FormSubmission.objects.count() == 1
