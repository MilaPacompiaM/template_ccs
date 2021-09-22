from django.urls import path

from .views import ImportView, ExportView


app_name = 'utils'


urlpatterns = [
    path('import/', ImportView.as_view()),
    path('export/', ExportView.as_view()),
]