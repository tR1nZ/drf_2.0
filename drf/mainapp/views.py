from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .models import User
from .serializer import UserSerializer, UserSerializerBase
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import mixins
from .filters import UserFilter
from rest_framework.pagination import LimitOffsetPagination


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def article_view(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    renderer_classes = [JSONRenderer]
    serializer_class = UserSerializer


class UserAPIView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserCreateAPIView(CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListAPIView(ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPIView(UpdateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDestroyAPIView(DestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    



    @action(detail=True, methods=['get'])
    
    def get_serializer_class(self):
        if self.request.version == '2.0':
            return UserSerializerBase
        return UserSerializer

    def user_text_only(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        return Response({'user.username': user.username})

    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserCustomViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]


class ArticleQuerysetFilterViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = User.objects.all()

    def get_queryset(self):
        return User.objects.filter(name__contains='python')


class ArticleKwargsFilterView(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return User.objects.filter(name__contains=name)


class ArticleDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['name', 'username']


class ArticleCustomDjangoFilterViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_class = UserFilter


class UserLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2


class ArticleLimitOffsetPaginationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserLimitOffsetPagination
