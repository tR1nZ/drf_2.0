import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import UserViewSet
from .models import User
class TestUserViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', {'username': 'pushkin', 'first_name': 'alex', 'lastname': 'pushkin', 'email': 'alexp1799'}, format='json')
        view = UserViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', {'username': 'pushkin', 'first_name': 'alex', 'lastname': 'pushkin', 'email': 'alexp1799'}, format='json')
        admin = User.objects.create_superuser('admin', 'admin@admin.com','admin123456')
        force_authenticate(request, admin)
        view = UserViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        user = User.objects.create(username = 'pushkin', first_name = 'alex', lastname = 'pushkin', email = 'alexp1799')
        client = APIClient()
        response = client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        user = User.objects.create(username = 'pushkin', first_name = 'alex', lastname = 'pushkin', email = 'alexp1799')
        client = APIClient()
        response = client.put(f'/api/users/{user.id}/', {'username': 'grin', 'first_name': 'alex', 'lastname': 'grin', 'email': 'alexg1880'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        user = User.objects.create(username = 'pushkin', first_name = 'alex', lastname = 'pushkin', email = 'alexp1799')
        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        client.login(username='admin', password='admin123456')
        response = client.put(f'/api/users/{user.id}/', {'username': 'grin', 'first_name': 'alex', 'lastname': 'grin', 'email': 'alexg1880'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = User.objects.get(id=user.id)
        self.assertEqual(user.username, 'grin')
        self.assertEqual(user.first_name, 'alex')
        self.assertEqual(user.last_name, 'grin')
        self.assertEqual(user.email, 'alexg1880')
        client.logout()


class TestMath(APISimpleTestCase):
    def test_sqrt(self):
        import math
        self.assertEqual(math.sqrt(4), 2)
