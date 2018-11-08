import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from .models import User


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = {
            'id': ['exact'],
            'name': ['exact', 'icontains', 'istartswith'],
            'username': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = [graphene.Node]
        # connection_class = CountableConnectionBase


class UserQuery(graphene.ObjectType):
    # users = DjangoFilterConnectionField(UserNode, filterset_class=UserFilter)
    users = DjangoFilterConnectionField(UserNode)
    user = graphene.Node.Field(UserNode)
