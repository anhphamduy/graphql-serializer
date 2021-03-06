import os
from unittest import TestCase

from graphql.language.ast import Document

from graphql_serializer.serializer import GraphqlSerializer

current_dir = os.path.dirname(os.path.abspath(__file__))
graphql_file = "data.graphql"
graphql_file_path = os.path.join(current_dir, graphql_file)


class SerializerTests(TestCase):

    def test_importing_graphql_type(self):
        graphql_object = GraphqlSerializer.read_graphql(graphql_file_path)

        self.assertIsNotNone(graphql_object)
        self.assertIsInstance(graphql_object, Document)
