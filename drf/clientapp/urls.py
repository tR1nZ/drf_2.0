from django.urls import path
from .views import ClientListAPIView

app_name = 'clientapp'
urlpatterns = [
    path('', ClientListAPIView.as_view()),
]
