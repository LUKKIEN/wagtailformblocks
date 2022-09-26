=====
Usage
=====

Once installed, ``wagtailformblocks`` are ready to be used.

It is shipped with an ``EmailForm`` model by default, based on wagtails own ``AbstractEmailForm`` page type.

Define custom form model
------------------------

If you want to define your own form model with it's own specific behaviour, simply subclass
the ``BaseForm`` class.

Example:

.. code-block:: python

    from django.db import models

    from wagtailformblocks.models import BaseForm


    class MyCustomForm(BaseForm):
        send_quotation = models.BooleanField(verbose_name=_('send me a quotation'), default=True)

        class Meta:
            verbose_name = _('My custom form')

        panels = BaseForm.panels + [
            FieldPanel('send_quotation',),
        ]

        def process_form_submission(self, form):
            super().process_form_submission(form)
            if self.send_quotation:
                # Do some extra stuff here

Your extra model will show up in the Wagtail CMS admin automatically.
