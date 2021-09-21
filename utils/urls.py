from django.urls import path

from .views import ImportView, ExportView


app_name = 'utils'


urlpatterns = [
    path('excel/import/', ImportView.as_view()),
    path('excel/export/', ExportView.as_view()),
]