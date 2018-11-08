from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

from eroapp.api.schema import schema

urlpatterns = [
    url(r'^graphiql', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    url(r'^graphql', csrf_exempt(GraphQLView.as_view(schema=schema))),
    url(r'^graphql/batch', csrf_exempt(GraphQLView.as_view(schema=schema, batch=True))),
]
