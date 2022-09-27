from django.utils.translation import gettext_lazy as _
from wagtail import hooks
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    ModelAdminGroup,
    modeladmin_register,
)

from .chooser import viewset
from .models import BaseForm, FormSubmission


def _get_valid_subclasses(klass):
    clss = []
    for subcls in klass.__subclasses__():
        if not getattr(subcls, 'wagtailformblocks_autoregister', True) or subcls._meta.abstract:
            pass
        else:
            clss.append(subcls)
        sub_classes = _get_valid_subclasses(subcls)
        if sub_classes:
            clss.extend(sub_classes)
    return clss


all_classes = _get_valid_subclasses(BaseForm)
form_admins = []

for cls in all_classes:
    object_name = cls._meta.object_name
    admin_name = "{}Admin".format(object_name)
    admin_defs = {
        'model': cls,
        'menu_label': cls._meta.verbose_name,
        'menu_icon': 'form',
    }
    admin_class = type(admin_name, (ModelAdmin, ), admin_defs)
    form_admins.append(admin_class)


class SubmissionAdmin(ModelAdmin):
    model = FormSubmission
    menu_icon = 'table'
    list_display = ('form_data', 'form', 'submit_time')
    list_filter = ('form', )


form_admins.append(SubmissionAdmin)


@modeladmin_register
class FormGroup(ModelAdminGroup):
    """A group where all the contact users go in
       todo: make the group so that we can add language to it
    """
    menu_label = _("User forms")
    menu_icon = 'form'
    menu_order = 500
    items = form_admins


@hooks.register("register_admin_viewset")
def register_image_chooser_viewset():
    return viewset
