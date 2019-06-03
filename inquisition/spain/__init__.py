from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker


class ClientConstructorTakesConfiguration(BaseChecker):
    __implements__ = IAstroidChecker

    name = "constructor-configuration"
    priority = -1
    msgs = {
        "C4712": (
            "Is missing a configuration parameter.",
            "missing-configuration-constructor-parameter",
            "All client types should accept a configuration parameter.",
        )
    }
    options = (
        (
            "ignore-configuration-missing-constuctor-parameter",
            {
                "default": False,
                "type": "yn",
                "metavar": "<y_or_n>",
                "help": "Allow client constructors without a configuration parameter",
            },
        ),
    )

    def __init__(self, linter=None):
        super().__init__(linter)
        self.is_client = []

    def visit_classdef(self, node):
        if node.name.endswith("Client"):
            self.is_client.append(True)
        else:
            self.is_client.append(False)

    def visit_functiondef(self, node):
        if node.name == "__init__" and self.is_client and self.is_client[-1]:
            # We are currently checking a client...
            arguments_node = next(
                (child for child in node.get_children() if child.is_argument)
            )
            if not "configuration" in [
                argument.name for argument in arguments_node.args
            ]:
                self.add_message(
                    msg_id="missing-configuration-constructor-parameter", node=node
                )


class ClientHasCreateConfigurationMethod(BaseChecker):
    __implements__ = IAstroidChecker

    name = "client-configuration-factory"
    priority = -1
    msgs = {
        "C4713": (
            "Is missing a create_configuration method.",
            "missing-configuration-factory-method",
            "All client types should have a create_configuration method.",
        ),
        "C4714": (
            "Is missing a **kwargs argument.",
            "missing-configuration-factory-method-kwargs",
            "All client types should have a create_configuration method that takes a **kwargs parameter.",
        ),
    }
    options = (
        (
            "ignore-missing-configuration-factory-method",
            {
                "default": False,
                "type": "yn",
                "metavar": "<y_or_n>",
                "help": "Allow clients to not have a create_configuration method",
            },
        ),
    )

    def __init__(self, linter=None):
        super().__init__(linter)
        self.is_client = []

    def visit_classdef(self, node):
        if node.name.endswith("Client"):
            try:
                configuration_function_def_node = next(
                    (
                        child
                        for child in node.get_children()
                        if child.is_function and child.name == "create_configuration"
                    )
                )
                arguments_node = next(
                    (
                        child
                        for child in configuration_function_def_node.get_children()
                        if child.is_argument
                    )
                )
                if not arguments_node.kwarg:
                    self.add_message(
                        msg_id="missing-configuration-factory-method-kwargs",
                        node=configuration_function_def_node,
                    )
            except StopIteration:
                self.add_message(
                    msg_id="missing-configuration-factory-method", node=node
                )



class ClientMethodReturnsTheRightThing(BaseChecker):
    __implements__ = IAstroidChecker

    name = "client-return-value"
    priority = -1
    msgs = {
        "C4715": (
            "Returns the wrong thing.",
            "service-method-incorrect-return-type",
            "The method does not return what it's name implies.",
        ),
    }
    options = (
        (
            "ignore-return-values",
            {
                "default": False,
                "type": "yn",
                "metavar": "<y_or_n>",
                "help": "Allow incorrect return values.",
            },
        ),
    )

    def __init__(self, linter=None):
        super().__init__(linter)
        self.is_client = []

    def visit_classdef(self, node):
        if node.name.endswith("Client"):
            try:
                configuration_function_def_node = next(
                    (
                        child
                        for child in node.get_children()
                        if child.is_function and child.name == "create_configuration"
                    )
                )
                arguments_node = next(
                    (
                        child
                        for child in configuration_function_def_node.get_children()
                        if child.is_argument
                    )
                )
                if not arguments_node.kwarg:
                    self.add_message(
                        msg_id="missing-configuration-factory-method-kwargs",
                        node=configuration_function_def_node,
                    )
            except StopIteration:
                self.add_message(
                    msg_id="missing-configuration-factory-method", node=node
                )


def register(linter):
    linter.register_checker(ClientConstructorTakesConfiguration(linter))
    linter.register_checker(ClientHasCreateConfigurationMethod(linter))

