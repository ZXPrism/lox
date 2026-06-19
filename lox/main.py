import argparse

from dataclasses import dataclass


@dataclass
class Token:
    pass


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

    def main(self):
        args = self.parser.parse_args()
        if args.script:
            self.run_file(args.script)
        else:
            self.run_repl()

    def run_file(self, src_path: str):
        with open(src_path, "r") as fp:
            self._run(fp.read())

    def run_repl(self):
        print("Lox 0.1.0 - b260615")

        while True:
            print(">", end=" ")
            line = input()
            self._run(line)

    def _run(self, src: str):
        scanner = Scanner(src)
        tokens = scanner.scan_tokens()
        for token in tokens:
            print(token)

    def _error(self, line_no: int, msg: str):
        self.report(line_no, "", msg)

    def _report(self, line_no: int, where: str, msg: str):
        print()


def entrypoint():
    engine = LoxEngine()
    engine.main()


if __name__ == "__main__":
    entrypoint()
