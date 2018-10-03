import json

from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.utils.translation import ugettext_lazy as _
from model_utils.managers import InheritanceManager
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel)
from wagtail.admin.utils import send_mail
from wagtail.contrib.forms.models import AbstractFormField

from .forms import FormBuilder
from .utils.conf import recaptcha_enabled


class FormSubmission(models.Model):
    """Data for a Form submission."""

    form_data = models.TextField()
    form = models.ForeignKey('BaseForm', on_delete=models.CASCADE)
    submit_time = models.DateTimeField(
        verbose_name=_('submit time'), auto_now_add=True)

    def get_data(self):
        return json.loads(self.form_data)

    def __str__(self):
        return self.form_data

    class Meta:
        verbose_name = _('form submission')


class FormField(AbstractFormField):
    form = ParentalKey('BaseForm', related_name='form_fields')


class BaseForm(ClusterableModel):
    name = models.CharField(max_length=255)
    store_submission = models.BooleanField(
        default=False,
        help_text=_('Store all form submissions in the database. This has to comply with local privacy laws.') # NOQA
    )
    add_recaptcha = models.BooleanField(
        default=False, help_text=_("Add a reCapcha field to the form."))
    success_message = models.CharField(
        blank=True,
        max_length=255,
        help_text=_('An optional success message to show when the form has been succesfully submitted') # NOQA
    )
    panels = [
        FieldPanel('name',),
        FieldPanel('store_submission',),
        FieldPanel('success_message'),
        InlinePanel('form_fields', label="Form fields"),
    ]

    objects = InheritanceManager()

    def __str__(self):
        return self.name

    def get_form_class(self):
        fb = FormBuilder(
            self.form_fields.all(), add_recaptcha=self.add_recaptcha)
        return fb.get_form_class()

    def get_form_parameters(self):
        return {}

    def get_form(self, *args, **kwargs):
        form_class = self.get_form_class()
        form_params = self.get_form_parameters()
        form_params.update(kwargs)

        return form_class(*args, **form_params)

    def process_form_submission(self, form):
        if self.store_submission:
            return FormSubmission.objects.create(
                form_data=json.dumps(form.cleaned_data, cls=DjangoJSONEncoder),
                form=self)


if recaptcha_enabled():
    BaseForm.panels.insert(2, FieldPanel('add_recaptcha'))


class EmailForm(BaseForm):
    """
    A Form Page that sends email. Pages implementing a form to be send
    to an email should inherit from it
    """

    to_address = models.CharField(
        verbose_name=_('to address'), max_length=255, blank=True,
        help_text=_("Optional - form submissions will be emailed to these addresses. Separate multiple addresses by comma.") # NOQA
    )
    from_address = models.CharField(
        verbose_name=_('from address'), max_length=255, blank=True)
    subject = models.CharField(
        verbose_name=_('subject'), max_length=255, blank=True)

    class Meta:
        verbose_name = _('Email form')

    panels = BaseForm.panels + [
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    def process_form_submission(self, form):
        super(EmailForm, self).process_form_submission(form)

        if self.to_address:
            self.send_form_mail(form)

    def send_form_mail(self, form):
        addresses = [x.strip() for x in self.to_address.split(',')]
        content = []
        for name, field in form.fields.items():
            data = form.cleaned_data.get(name)
            if name == 'recaptcha' or not data:
                continue
            content.append(
                field.label + ': ' + str(data))

        send_mail(
            self.subject, '\n'.join(content), addresses, self.from_address)
