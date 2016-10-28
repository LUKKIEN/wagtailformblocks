from django.conf import settings
from wagtail.wagtailforms.forms import FormBuilder as OrigFormBuilder

from wagtailformblocks.utils.conf import get_formblocks_setting

try:
    from captcha.fields import ReCaptchaField
    RECAPTCHA_ENABLED = (
        'captcha' in settings.INSTALLED_APPS and
        getattr(settings, 'RECAPTCHA_PUBLIC_KEY', False) and
        getattr(settings, 'RECAPTCHA_PRIVATE_KEY', False)
    )
except ImportError:
    RECAPTCHA_ENABLED = False


class FormBuilder(OrigFormBuilder):

    def __init__(self, fields, **kwargs):
        self.add_recaptcha = kwargs.pop('add_recaptcha')
        super(FormBuilder, self).__init__(fields)

    @property
    def formfields(self):
        formfields = super(FormBuilder, self).formfields

        if RECAPTCHA_ENABLED and self.add_recaptcha:
            recaptcha_attrs = get_formblocks_setting('RECAPTCHA_ATTRS')
            formfields['recaptcha'] = ReCaptchaField(attrs=recaptcha_attrs)

        return formfields
