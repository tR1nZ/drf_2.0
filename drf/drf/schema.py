import graphene
from graphene_django import DjangoObjectType
from mainapp.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


"""class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'"""

class Query(graphene.ObjectType):
    
    all_users = graphene.List(UserType)
    user_by_id = graphene.Field(UserType, id=graphene.Int(required=True))

    def resolve_all_authors(root, info):
        return User.objects.all()

    def resolve_author_by_id(self, info, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None

    """def resolve_all_books(root, info):
        return Book.objects.all()
    """

class UserMutation(graphene.Mutation):
    class Arguments:
        birthday_year = graphene.Int(required=True)
        id = graphene.ID()

    author = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, username, id):
        user = User.objects.get(pk=id)
        user.username = username
        user.save()
        return UserMutation(user=user)

class Mutation(graphene.ObjectType):
    update_author = UserMutation.Field()



schema = graphene.Schema(query=Query, mutation=Mutation)
 