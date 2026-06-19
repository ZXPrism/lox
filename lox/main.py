import argparse

from dataclasses import dataclass
from enum import IntEnum


class TokenType(IntEnum):
    # Single-character tokens.
    LEFT_PAREN = 1  # (
    RIGHT_PAREN = 2  # )
    LEFT_BRACE = 3  # {
    RIGHT_BRACE = 4  # }
    COMMA = 5  # ,
    DOT = 6  # .
    MINUS = 7  # -
    PLUS = 8  # +
    SEMICOLON = 9  # ;
    SLASH = 10  # /
    STAR = 11  # *

    # One or two character tokens.
    BANG = 12  # !
    BANG_EQUAL = 13  # !=
    EQUAL = 14  # =
    EQUAL_EQUAL = 15  # ==
    GREATER = 16  # >
    GREATER_EQUAL = 17  # >=
    LESS = 18  # <
    LESS_EQUAL = 19  # <=

    # Literals.
    IDENTIFIER = 20
    STRING = 21
    NUMBER = 22

    # Keywords.
    AND = 23
    CLASS = 24
    ELSE = 25
    FALSE = 26
    FUN = 27
    FOR = 28
    IF = 29
    NIL = 30
    OR = 31
    PRINT = 32
    RETURN = 33
    SUPER = 34
    THIS = 35
    TRUE = 36
    VAR = 37
    WHILE = 38

    EOF = 39


@dataclass
class Token:
    type: TokenType
    lexeme: str
    literal: object
    line_no: int

    def to_string(self) -> str:
        return f"{self.type.name} {self.lexeme} {self.literal}"


class Scanner:
    def __init__(self, src: str):
        pass

    def scan_tokens(self) -> list[Token]:
        return []


class LoxEngine:
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog="lox",
            description="Lox language interpreter",
        )
        self.parser.add_argument(
            "script",
            nargs="?",
            help="Path to a Lox script to execute",
        )

        self.had_error = False

    def main(self):
        args = self.parser.parse_args()
        if args.script:
            self.run_file(args.script)
        else:
            self.run_repl()

    def run_file(self, src_path: str):
        with open(src_path, "r") as fp:
            self._run(fp.read())
            if self.had_error:
                exit(65)

    def run_repl(self):
        print("Lox 0.1.0 - b260615")

        while True:
            print(">", end=" ")
            line = input()
            self._run(line)
            self.had_error = False

    def _run(self, src: str):
        scanner = Scanner(src)
        tokens = scanner.scan_tokens()
        for token in tokens:
            print(token)

    def _error(self, line_no: int, msg: str):
        self._report(line_no, "", msg)

    def _report(self, line_no: int, where: str, msg: str):
        print(f"[line {line_no}] Error{where}: {msg}")
        self.had_error = True


def entrypoint():
    engine = LoxEngine()
    engine.main()


if __name__ == "__main__":
    entrypoint()
