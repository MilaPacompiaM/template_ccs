from django.urls import path

from .views import PDFView


app_name = 'utils'


urlpatterns = [
    path('pdf/', PDFView.as_view()),
]