from abc import ABC, abstractmethod
from dataclasses import dataclass
from lox.token import Token


class AstVisitor(ABC):

    @abstractmethod
    def visit_binary(self, expr: "Binary") -> object: ...

    @abstractmethod
    def visit_grouping(self, expr: "Grouping") -> object: ...

    @abstractmethod
    def visit_literal(self, expr: "Literal") -> object: ...

    @abstractmethod
    def visit_unary(self, expr: "Unary") -> object: ...



class Expression(ABC):
    @abstractmethod
    def accept(self, visitor: AstVisitor) -> object | None: ...


@dataclass
class Binary(Expression):
    left: Expression
    operator: Token
    right: Expression

    def accept(self, visitor: AstVisitor) -> object | None:
        return visitor.visit_binary(self)


@dataclass
class Grouping(Expression):
    expression: Expression

    def accept(self, visitor: AstVisitor) -> object | None:
        return visitor.visit_grouping(self)


@dataclass
class Literal(Expression):
    value: object | None

    def accept(self, visitor: AstVisitor) -> object | None:
        return visitor.visit_literal(self)


@dataclass
class Unary(Expression):
    operator: Token
    right: Expression

    def accept(self, visitor: AstVisitor) -> object | None:
        return visitor.visit_unary(self)

