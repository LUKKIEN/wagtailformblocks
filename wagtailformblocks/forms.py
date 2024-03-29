from captcha.fields import ReCaptchaField
from wagtail.contrib.forms.forms import FormBuilder as OrigFormBuilder

from wagtailformblocks.utils.conf import get_formblocks_setting, recaptcha_enabled


class FormBuilder(OrigFormBuilder):

    def __init__(self, fields, **kwargs):
        self.add_recaptcha = kwargs.pop('add_recaptcha')
        super().__init__(fields)

    @property
    def recaptcha_enabled(self):
        return self.add_recaptcha and recaptcha_enabled()

    @property
    def formfields(self):
        formfields = super().formfields

        if self.recaptcha_enabled:
            recaptcha_attrs = get_formblocks_setting('RECAPTCHA_ATTRS')
            formfields['recaptcha'] = ReCaptchaField(**recaptcha_attrs)

        return formfields
