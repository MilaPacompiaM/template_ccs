from django.http import HttpResponse

from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes

from .files import ExcelManager
from .constants import Template


@permission_classes((permissions.AllowAny,))
class ImportView(APIView):
    authentication_classes = []

    def post(self, request):
        file = request.FILES.getlist('file')[0]
        valueset = ExcelManager.read_values(file, Template.DEMO_READER)
        return Response({'filename': file.name, 'values': valueset})

@permission_classes((permissions.AllowAny,))
class ExportView(APIView):
    authentication_classes = []

    def post(self, request):
        wb = ExcelManager.write(request.data, Template.DEMO_WRITER)
        response = HttpResponse(content_type='text/xls')
        response['Content-Disposition'] = 'attachment; filename=prueba.xls'
        wb.save(response)
        return response
