# graphql_api.py
from flask import Blueprint
from flask_graphql import GraphQLView
from graphql_schema import schema

graphql_api = Blueprint("graphql_api", __name__)

graphql_api.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)
