from django.test import TestCase, override_settings

from tests.test_wagtailformblocks import make_formfields
from wagtailformblocks.models import BaseForm


class TestFormBuilder(TestCase):

    def setUp(self):
        self.baseform = BaseForm.objects.create()
        make_formfields(self.baseform)

    @override_settings(
        INSTALLED_APPS=['captcha'],
        RECAPTCHA_PUBLIC_KEY='public-key',
        RECAPTCHA_PRIVATE_KEY='private-key'
    )
    def test_add_recaptcha(self):
        form = self.baseform.get_form()
        self.assertNotIn('recaptcha', form.fields)

        self.baseform.add_recaptcha = True
        self.baseform.save()

        form = self.baseform.get_form()
        self.assertIn('recaptcha', form.fields)

