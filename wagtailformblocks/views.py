from django.http import JsonResponse
from django.views.generic import View

from .models import BaseForm
from .utils.conf import get_formblocks_setting


class FormProcessView(View):
    """ Return office information as Json"""
    http_method_names = ['post', ]

    def post(self, request, pk):
        try:
            formdef = BaseForm.objects.get_subclass(id=pk)
        except BaseForm.DoesNotExist:
            err = {
                'message': str(get_formblocks_setting('ERROR_MSG')), # NOQA
                'detail': 'Could not find WagtailForm with id {}'.format(pk)
            }
            return JsonResponse(err, status=400)

        form = formdef.get_form(request.POST)

        if form.is_valid():
            formdef.process_form_submission(form)
        else:
            err = {
                'message': str(get_formblocks_setting('ERROR_MSG')),  # NOQA
                'detail': form.errors
            }
            return JsonResponse(err, status=400)

        resp = {
            'message': formdef.success_message or str(
                get_formblocks_setting('SUCCESS_MSG')
            )
        }
        return JsonResponse(resp)
