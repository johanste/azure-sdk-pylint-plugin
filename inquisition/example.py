""" This is an example of a pylint-clean client
"""

class MyExampleClient:
    """ A simple, canonical client
    """

    def __init__(self, base_url, configuration):
        """ This constructor follows the canonical pattern.

        - It has a configuration parameter.
        """

    def create_configuration(self, **kwargs):
        """ All methods should allow for a configuration instance to be created.
        """

    def get_thing(self, name):
        # type: (str) -> Thing
        """ Getting a single instance should include a required parameter

        - The first positional parameter should be a name or some other identifying
        attribute of the `thing`.
        """
        

    def list_things(self):
        """ Getting a list of instances should not include any required parameters.
        """
