import os
from unittest import TestCase

from graphql_serializer.objects import GraphqlObjectType
from graphql_serializer.preprocessing import GraphqlPreprocessing

current_dir = os.path.dirname(os.path.abspath(__file__))
graphql_file = "data.graphql"
graphql_file_path = os.path.join(current_dir, graphql_file)


class PreprocessingTests(TestCase):

    def test_importing_graphql_type(self):
        graphql_object = GraphqlPreprocessing.read_graphql(graphql_file_path)
        
        self.assertIsNotNone(graphql_object)
        self.assertIsInstance(graphql_object, GraphqlObjectType)
