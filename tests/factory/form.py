import factory

from wagtailformblocks.models import BaseForm, EmailForm


class BaseFormFactory(factory.DjangoModelFactory):
    class Meta:
        model = BaseForm

    name = 'BaseForm'


class EmailFormFactory(factory.DjangoModelFactory):
    class Meta:
        model = EmailForm

    name = 'EmailForm'
