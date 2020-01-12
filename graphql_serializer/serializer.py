from gql import gql


class GraphqlSerializer:
    @staticmethod
    def serialize():
        raise NotImplementedError

    @staticmethod
    def read_graphql(file_path):
        """
        Read in the content of a graphql file and output a GraphqlObjectType

        Arguments:
            file_path {str} -- The path to the file

        Returns:
            graphql.language.ast.Document -- A Graphql document
        """

        with open(file_path, "r") as f:
            file_content = f.read()
            return gql(file_content)
