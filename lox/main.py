import argparse


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
        print(src_path)

    def run_repl(self):
        print("Lox 0.1.0 - b260615")


def entrypoint():
    engine = LoxEngine()
    engine.main()


if __name__ == "__main__":
    entrypoint()
