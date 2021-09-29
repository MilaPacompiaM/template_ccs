from django.test import Client

from rest_framework import status
from rest_framework.test import APITestCase


class ImportViewTest(APITestCase):

    def setUp(self):
        self.url = '/api/utils/import/'
        self.client = Client()

    def test_import_csv(self):
        filename = 'Ejemplo.csv'
        with open('utils/test_files/{}'.format(filename)) as file:
            response = self.client.post(self.url, {'file': file})
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)
            self.assertEqual(response.data.get('filename'), filename)
            self.assertDictContainsSubset(
                {'nombre': '"Juan Perez"', 'edad': '"30"'},
                response.data.get('values')
            )

    def test_import_excel(self):
        filename = 'Ejemplo.xlsx'
        with open('utils/test_files/{}'.format(filename), 'rb') as file:
            response = self.client.post(self.url, {'file': file})
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertIsNotNone(response.data)
            self.assertEqual(response.data.get('filename'), filename)
            self.assertDictContainsSubset(
                {'nombre': 'Juan Perez', 'edad': 30},
                response.data.get('values')
            )


class ExportViewTest(APITestCase):

    def setUp(self):
        self.url = '/api/utils/export/'
        self.client = Client()
    
    def test_export_csv(self):
        data = {
            'extension': 'csv',
            'datamap': {
                'name': 'Mila',
                'age': 24
            }
        }
        response = self.client.post(
            self.url, data=data, content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_export_excel(self):
        data = {
            'extension': 'xls',
            'datamap': {
                'name': 'Mila',
                'age': 24
            }
        }
        response = self.client.post(
            self.url, data=data, content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_export_pdf(self):
        data = {
            'extension': 'pdf',
            'datamap': {
                'name': 'Mila',
                'result': 10
            }
        }
        response = self.client.post(
            self.url, data=data, content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
