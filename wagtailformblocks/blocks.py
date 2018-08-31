from __future__ import absolute_import, unicode_literals

from django import forms
from django.urls import reverse

from wagtail.core import blocks

from .models import BaseForm


class FormChooserBlock(blocks.ChooserBlock):
    target_model = BaseForm
    widget = forms.Select

    def value_for_form(self, value):
        if isinstance(value, self.target_model):
            return value.pk
        return value

    def to_python(self, value):
        # the incoming serialised value should be None or an ID
        if value is None:
            return value
        else:
            try:
                if hasattr(self.target_model.objects, 'get_subclass'):
                    return self.target_model.objects.get_subclass(pk=value)
                return self.target_model.objects.get(pk=value)
            except self.target_model.DoesNotExist:
                return None


class WagtailFormBlock(blocks.StructBlock):
    form = FormChooserBlock()

    class Meta:
        icon = 'icon icon-form'
        template = 'wagtailformblocks/form_block.html'

    def get_action_url(self, form):
        return reverse('wagtailformblocks_process', kwargs={'pk': form.id})

    def get_context(self, value, parent_context=None):
        if not parent_context:
            context = super(WagtailFormBlock, self).get_context(value)
        else:
            context = super(WagtailFormBlock, self).get_context(value, parent_context)

        form = value['form']

        context['form'] = form.get_form()
        context['form_id'] = form.id
        context['action_url'] = self.get_action_url(form)
        return context
