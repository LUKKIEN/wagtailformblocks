from __future__ import absolute_import, print_function, unicode_literals

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BaseForm
from .utils.conf import get_formblocks_setting


class FormProcessView(APIView):
    """ Return office information as Json"""
    def post(self, request, pk):
        try:
            formdef = BaseForm.objects.get_subclass(id=pk)
        except BaseForm.DoesNotExist:
            err = {
                'message': get_formblocks_setting('ERROR_MSG'),
                'detail': 'Could not find WagtailForm with id {}'.format(pk)
            }
            return Response(err, status=status.HTTP_400_BAD_REQUEST)

        form = formdef.get_form(request.data)

        if form.is_valid():
            formdef.process_form_submission(form)
        else:
            err = {
                'message': get_formblocks_setting('ERROR_MSG'),
                'detail': form.errors
            }
            return Response(err, status=status.HTTP_400_BAD_REQUEST)

        resp = {
            'message': formdef.success_message or get_formblocks_setting('SUCCESS_MSG')
        }
        return Response(resp)
