from django.urls import reverse
from django.utils.functional import cached_property
from wagtail.core import blocks

from .models import BaseForm


class FormChooserBlock(blocks.ChooserBlock):
    target_model = BaseForm

    def value_for_form(self, value):
        return value.pk if isinstance(value, self.target_model) else value

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

    @cached_property
    def widget(self):
        from wagtailformblocks.widgets import FormChooserWidget

        return FormChooserWidget()


class WagtailFormBlock(blocks.StructBlock):
    form = FormChooserBlock()

    class Meta:
        icon = 'form'
        template = 'wagtailformblocks/form_block.html'

    def get_action_url(self, form):
        return reverse('wagtailformblocks_process', kwargs={'pk': form.id})

    def get_context(self, value, parent_context=None):
        if not parent_context:
            context = super().get_context(value)
        else:
            context = super().get_context(value, parent_context)

        form = value['form']

        return {
            'form': form.get_form(),
            'form_id': form.id,
            'action_url': self.get_action_url(form),
            **context,
        }
