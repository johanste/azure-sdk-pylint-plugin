import astroid
import pylint.testutils

import spain


class TestClientHasConfiguration(pylint.testutils.CheckerTestCase):
    CHECKER_CLASS = spain.ClientConstructorTakesConfiguration

    def test_finds_missing_config_parameter(self):
        class_node, constructor_a = astroid.extract_node(
            """
        class SomeClient(): #@

            def __init__(self, some, arguments, **kwargs): #@
                pass
        """
        )

        self.checker.visit_classdef(class_node)
        with self.assertAddsMessages(
            pylint.testutils.Message(
                msg_id="missing-configuration-constructor-parameter", node=constructor_a
            )
        ):
            self.checker.visit_functiondef(constructor_a)

    def test_finds_config_parameter(self):
        class_node, constructor_a = astroid.extract_node(
            """
        class SomeClient(): #@

            def __init__(self, some, configuration, **kwargs): #@
                pass
        """
        )

        self.checker.visit_classdef(class_node)
        with self.assertNoMessages():
            self.checker.visit_functiondef(constructor_a)

    def test_ignores_non_client_missing_config_parameter(self):
        class_node, constructor_a = astroid.extract_node(
            """
        class SomethineElse(): #@

            def __init__(self, some, **kwargs): #@
                pass
        """
        )

        self.checker.visit_classdef(class_node)
        with self.assertNoMessages():
            self.checker.visit_functiondef(constructor_a)


    def test_ignores_nested_function_missing_config_parameter(self):
        class_node, constructor_a = astroid.extract_node(
            """
            class SomethineElse(): #@

                def __init__(self, some, **kwargs): #@
                    def nested(hello, world):
                        pass
            """
        )

        self.checker.visit_classdef(class_node)
        with self.assertNoMessages():
            self.checker.visit_functiondef(constructor_a)
