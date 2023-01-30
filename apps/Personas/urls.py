from django.urls import path as p
from graphene_django.views import GraphQLView

from .schema import schema

urlpatterns = [
    p('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]
