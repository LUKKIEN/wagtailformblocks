from django.utils.translation import gettext_lazy as _
from wagtail.admin.viewsets.chooser import ChooserViewSet

from wagtailformblocks.models import BaseForm


class ImageChooserViewSet(ChooserViewSet):
    icon = "form"
    choose_one_text = _("Choose a form")
    register_widget = False


viewset = ImageChooserViewSet("wagtailformblocks_chooser", model=BaseForm, url_prefix="wagtailformblocks/chooser")
