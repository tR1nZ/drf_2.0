"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from mainapp.views import UserModelViewSet
from mainapp import views
from rest_framework.authtoken import views as view
from clientapp.views import ClientListAPIView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
#from graphene_django.views import GraphQLView


schema_view = get_schema_view(
    openapi.Info(
    title="Library",
        default_version='0.1',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    #permission_classes=[permissions.AllowAny],
)


router = DefaultRouter()
router.register('users', UserModelViewSet)

urlpatterns = [
    path('api-token-auth/', view.obtain_auth_token),
    path('viewsets/', include(router.urls)),
    path('views/api-view/', views.UserAPIView.as_view()),
    path('generic/retrieve/<int:pk>/', views.UserRetrieveAPIView.as_view()),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('filters/kwargs/<str:name>/', views.ArticleKwargsFilterView.as_view()),
    re_path(r'^api/(?P<version>\d\.\d)/clients/$', ClientListAPIView.as_view()),
    path('api/clients/0.1', include('clientapp.urls', namespace='0.1')),
    path('api/clients/0.2', include('clientapp.urls', namespace='0.2')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #path("graphql/", GraphQLView.as_view(graphiql=True)),

]
