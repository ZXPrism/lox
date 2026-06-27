from graphviz import Digraph
from lox.token import Token, TokenType
from lox.ast_types import AstVisitor, Expression, Binary, Grouping, Literal, Unary


class AstPrinter(AstVisitor):
    def print(self, expr: Expression):
        self.dot = Digraph(comment="AST")
        self.dot.graph_attr["rankdir"] = "BT"

        self.node_id = 0
        self.parent = -1

        expr.accept(self)

        self.dot.render("ast_render", format="png", cleanup=True)

    def _make_node(self, caption: str):
        self.dot.node(str(self.node_id), caption)

    def _make_edge(self):
        if self.parent != -1:
            self.dot.edge(str(self.node_id), str(self.parent))

    def visit_binary(self, expr: Binary) -> object | None:
        self.node_id += 1
        self._make_node(expr.operator.lexeme)
        self._make_edge()

        node_id = self.node_id

        self.parent = node_id
        expr.left.accept(self)

        self.parent = node_id
        expr.right.accept(self)

    def visit_grouping(self, expr: Grouping) -> object | None:
        self.node_id += 1
        self._make_node("( )")
        self._make_edge()

        self.parent = self.node_id
        expr.expression.accept(self)

    def visit_literal(self, expr: Literal) -> object | None:
        self.node_id += 1
        caption = "nil"
        if expr.value is not None:
            caption = (
                str(expr.value)
                if isinstance(expr.value, int) or isinstance(expr.value, float)
                else f'"{expr.value}"'
            )
        self._make_node(caption)
        self._make_edge()

    def visit_unary(self, expr: Unary) -> object | None:
        self.node_id += 1
        self._make_node(expr.operator.lexeme)
        self._make_edge()

        self.parent = self.node_id
        expr.right.accept(self)


if __name__ == "__main__":
    ast_printer = AstPrinter()
    ast_printer.print(
        Binary(
            left=Unary(
                operator=Token(
                    type=TokenType.MINUS, lexeme="-", literal=None, line_no=1
                ),
                right=Literal(value=123),
            ),
            operator=Token(type=TokenType.STAR, lexeme="*", literal=None, line_no=1),
            right=Grouping(expression=Literal(value=45.67)),
        )
    )
