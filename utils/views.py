import csv

from django.http import HttpResponse

from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import permission_classes

from .files import ExcelManager, CsvManager, PDFManager
from .constants import Template


@permission_classes((permissions.AllowAny,))
class ImportView(APIView):
    authentication_classes = []

    def post(self, request):
        file = request.FILES.getlist('file')[0]
        FileManager = (
            CsvManager if file.name.endswith('.csv') else ExcelManager
        )
        valueset = FileManager.read_values(file, Template.DEMO_READER)
        return Response({'filename': file.name, 'values': valueset})


@permission_classes((permissions.AllowAny,))
class ExportView(APIView):
    authentication_classes = []

    def post(self, request):
        data = request.data
        datamap = data.get('datamap', {})
        extension = data.get('extension', 'csv')
        response = HttpResponse(content_type='text/{}'.format(extension))
        response['Content-Disposition'] = (
            "attachment; filename=Prueba.{}".format(extension)
        )
        if extension == 'csv':
            writer = csv.writer(response)
            datafile = CsvManager.write(datamap, Template.DEMO_WRITER)
            [writer.writerow([column for column in item]) for item in datafile]
            return response
        elif extension == 'pdf':
            pdf = PDFManager.write(datamap, request=request)
            response.content = pdf
            return response
        else:
            wb = ExcelManager.write(datamap, Template.DEMO_WRITER)
            wb.save(response)
            return response
