from django.http import HttpResponse

from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


@permission_classes((permissions.AllowAny,))
class PDFView(APIView):
    authentication_classes = []

    def post(self, request):
        file = request.FILES.getlist('file')[0]
        print('file: ', file.name)
        return Response({'filename': file.name})

