"""Unit tests for pylint_blank_line_plugin/checker."""

import unittest

import astroid
from pylint import testutils

from pylint_no_blank_line import checker


class TestUniqueReturnChecker(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.checker_test_object = testutils.CheckerTestCase()
        self.checker_test_object.CHECKER_CLASS = (
            checker.NoBlankLineAfterFunctionDefChecker)
        self.checker_test_object.setup_method()

    def test_function_with_blank_line_after_function_definition(
        self
    ) -> None:
        node = astroid.extract_node(
            """def add(first: int, second: int) -> int:

                   return first+second
            """)
        with self.checker_test_object.assertAddsMessages(
            testutils.MessageTest(
                msg_id='Blank-line-after-function-definition',
                node=node,
                line=2,
                col_offset=0,
                end_line=1,
                end_col_offset=8
            )
        ):
            self.checker_test_object.checker.visit_functiondef(
                node)

    def test_function_with_no_blank_line_after_function_definition(
        self
    ) -> None:
        node = astroid.extract_node(
            """def add(first: int, second: int) -> int:
                   '''This is a docstring.'''
                   return first+second
            """)
        with self.checker_test_object.assertNoMessages():
            self.checker_test_object.checker.visit_functiondef(
                node)
