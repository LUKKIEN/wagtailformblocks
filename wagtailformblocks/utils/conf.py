from django import VERSION as DJANGO_VERSION
from django.conf import settings

if DJANGO_VERSION < (3, 0):
    from django.utils.translation import ugettext_lazy as _
else:
    from django.utils.translation import gettext_lazy as _


DEFAULTS = {
    'SUCCESS_MSG': _('Thank you, the form has been submitted.'),
    'ERROR_MSG': _('There was an error processing the form'),
    'RECAPTCHA_ATTRS': {}
}


def get_formblocks_setting(name):
    return getattr(
        settings, 'WAGTAIL_FORMBLOCKS_{}'.format(name), DEFAULTS[name])


def recaptcha_enabled():
    return (
        'captcha' in settings.INSTALLED_APPS
        and getattr(settings, 'RECAPTCHA_PUBLIC_KEY', False)
        and getattr(settings, 'RECAPTCHA_PRIVATE_KEY', False)
    )
