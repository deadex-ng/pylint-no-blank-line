"""Unit tests for pylint_blank_line_plugin/checker."""
import unittest

import astroid
import pylint.testutils
from pylint_no_blank_line import checker


class TestNoBlankLineAfterFunctionDefChecker(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.checker_test_object = pylint.testutils.CheckerTestCase()
        self.checker_test_object.CHECKER_CLASS = (
            checker.NoBlankLineAfterFunctionDefChecker
        )
        self.checker_test_object.setup_method()

    def test_function_with_blank_line_after_function_definition(self) -> None:
        node = astroid.extract_node(
            """def func_one(num: int):

                   return num
            """
        )
        with self.checker_test_object.assertAddsMessages(
            pylint.testutils.MessageTest(
                msg_id="Blank-line-after-function-definition",
                line=2,
                node=node,
                col_offset=0,
                end_line=1,
                end_col_offset=12,
            )
        ):
            self.checker_test_object.checker.visit_functiondef(node)

    def test_function_with_blank_line_after_function_definition_and_with_docs(
        self,
    ) -> None:
        node = astroid.extract_node(
            """def func_one(num: int):
                   '''Funtion inside a docstring.

                      def doc_func():

                        return 4
                   '''
                   return num
            """
        )
        with self.checker_test_object.assertNoMessages():
            self.checker_test_object.checker.visit_functiondef(node)

    def test_function_with_blank_line_after_function(self) -> None:
        node = astroid.extract_node(
            """def func_one(num: int):
                   '''Funtion inside a docstring.

                      def doc_func():

                        return 4
                   '''

                   return num
            """
        )
        with self.checker_test_object.assertAddsMessages(
            pylint.testutils.MessageTest(
                msg_id="Blank-line-after-function-definition",
                line=8,
                node=node,
                col_offset=0,
                end_line=1,
                end_col_offset=12,
            )
        ):
            self.checker_test_object.checker.visit_functiondef(node)
