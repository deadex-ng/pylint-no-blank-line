"""Custom checker that ensures that there is no blank line after function definition"""
import linecache

import astroid
from pylint import interfaces
from pylint import checkers


class NoBlankLineAfterFunctionDefChecker(checkers.BaseChecker):
    """Ensures that there is no blank line after function definition"""

    __implements__ = (interfaces.IAstroidChecker,)

    name = "awesome-checker"

    msgs = {
        "W9039": (
            "Blank line after function definition",
            "Blank-line-after-function-definition",
            "Please remove blank line after function definition",
        )
    }

    def visit_functiondef(self, node: astroid.nodes.FunctionDef) -> None:
        """Called for function and method definitions (def).

        Args:
            node: astroid.scoped_nodes.FunctionDef. Node for a function or
                method definition in the AST.
        """
        if node.doc_node:
            if (
                len(node.doc_node.value.split("\n")) + node.position.lineno
                == node.tolineno
            ):
                return
            if (
                len(node.doc_node.value.split("\n")) + node.position.lineno + 1
                == node.tolineno
            ):
                return
            if (
                len(node.doc_node.value.split("\n")) + node.position.lineno + 1
                < node.tolineno
            ):
                if not node.args.args:
                    num = (
                        len(node.doc_node.value.split("\n")) + node.position.lineno + 1
                    )
                    line = linecache.getline(node.root().file, num)
                    if not line.strip():
                        self.add_message(
                            "Blank-line-after-function-definition", line=num, node=node
                        )
                if node.args.args:
                    line = linecache.getline(node.root().file, node.position.lineno)
                    if line.endswith(":\n"):
                        line_number = (
                            len(node.doc_node.value.split("\n"))
                            + node.position.lineno
                            + 1
                        )
                        line = linecache.getline(node.root().file, line_number)
                        if not line.strip():
                            self.add_message(
                                "Blank-line-after-function-definition",
                                line=line_number,
                                node=node,
                            )
                    else:
                        line_number = node.position.lineno
                        while not line.endswith(":\n"):
                            line_number = line_number + 1
                            line = linecache.getline(node.root().file, line_number)
                        line_number = (
                            len(node.doc_node.value.split("\n")) + line_number + 1
                        )
                        line = linecache.getline(node.root().file, line_number)
                        if not line.strip():
                            self.add_message(
                                "Blank-line-after-function-definition",
                                line=line_number,
                                node=node,
                            )
        if node.doc_node is None:
            line_number = node.position.lineno + 1
            line = linecache.getline(node.root().file, line_number)
            if not line.strip():
                self.add_message(
                    "Blank-line-after-function-definition",
                    line=line_number,
                    node=node,
                )
