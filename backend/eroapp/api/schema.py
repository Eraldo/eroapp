import graphene
from graphene_django.debug import DjangoDebug

from eroapp.users.schema import UserQuery


class Query(
    UserQuery,
    graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')


# class Mutation(
#     graphene.ObjectType):
#     pass


# schema = graphene.Schema(query=Query, mutation=Mutation)
schema = graphene.Schema(query=Query)
