from .objects import GraphqlObjectType


class GraphqlPreprocessing:

    @staticmethod
    def read_graphql(file_path):
        """
        Read in the content of a graphql file and output a GraphqlObjectType

        Arguments:
            file_path {str} -- The path to the file

        Returns:
            GraphqlObjectType -- A GraphqlObjectType of the content of the file
        """
        raise NotImplementedError
