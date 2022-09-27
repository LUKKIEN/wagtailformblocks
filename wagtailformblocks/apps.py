from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WagtailFormBlocksAppConfig(AppConfig):
    name = "wagtailformblocks"
    label = "wagtailformblocks"
    verbose_name = _("Wagtail form blocks")
    default_auto_field = "django.db.models.AutoField"
