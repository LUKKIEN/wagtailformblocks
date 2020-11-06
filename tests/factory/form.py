import factory

from wagtailformblocks.models import BaseForm, EmailForm


class BaseFormFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BaseForm

    name = 'BaseForm'


class EmailFormFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EmailForm

    name = 'EmailForm'
