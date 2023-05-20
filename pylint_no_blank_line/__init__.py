"""Module to register checker."""
from pylint.lint import PyLinter

from pylint_no_blank_line.checker import NoBlankLineAfterFunctionDefChecker


def register(linter: PyLinter) -> None:
    """Registers the checker with pylint.

    Args:
        linter: Pylinter. The Pylinter object.
    """
    linter.register_checker(NoBlankLineAfterFunctionDefChecker(linter))
