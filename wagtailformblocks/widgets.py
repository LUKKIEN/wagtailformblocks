import json

from django.utils.translation import gettext_lazy as _
from wagtail.admin.widgets import BaseChooser, BaseChooserAdapter
from wagtail.telepath import register

from wagtailformblocks.models import BaseForm


class FormChooserWidget(BaseChooser):
    model = BaseForm
    choose_one_text = _("Choose a form")
    chooser_modal_url_name = "wagtailformblocks_chooser:choose"
    icon = "form"

    def render_js_init(self, id_, name, value_data):
        return f"new FormChooserWidget({json.dumps(id_)});"


register(BaseChooserAdapter(), FormChooserWidget)
