from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import ClientSerializer, ClientSerializerWithFullName

class ClientListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = ClientSerializer
    def get_serializer_class(self):
        if self.request.version == '0.2':
            return ClientSerializerWithFullName
        return ClientSerializer