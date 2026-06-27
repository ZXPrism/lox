import argparse

from rich import print
from lox.scanner import Scanner


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
        scanner = Scanner(src, lambda line_no, msg: self._error(line_no, msg))
        tokens = scanner.scan_tokens()
        for token in tokens:
            print(token)

    def _error(self, line_no: int, msg: str):
        self._report_error(line_no, "", msg)

    def _report_error(self, line_no: int, where: str, msg: str):
        print(f"[line {line_no}] Error{where}: {msg}")
        self.had_error = True


def entrypoint():
    engine = LoxEngine()
    engine.main()


if __name__ == "__main__":
    entrypoint()
