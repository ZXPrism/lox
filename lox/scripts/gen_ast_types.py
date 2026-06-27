import argparse

from pathlib import Path
from jinja2 import Environment, FileSystemLoader


def entrypoint(argv=None):
    parser = argparse.ArgumentParser(
        prog="gen_ast_types",
        description="Lox AST types generator",
    )
    parser.add_argument("-o", "--output", required=True, help="output path")
    args = parser.parse_args() if argv is None else parser.parse_args(argv)

    env = Environment(loader=FileSystemLoader(Path(__file__).parent))
    template = env.get_template("ast_types.py.jinja2")

    src = template.render(
        base_class_name="Expression",
        visitor_class_name="AstVisitor",
        types=[
            _make_type(
                "Binary", ["Expression left", "Token operator", "Expression right"]
            ),
            _make_type("Grouping", ["Expression expression"]),
            _make_type("Literal", ["object | None value"]),
            _make_type("Unary", ["Token operator", "Expression right"]),
        ],
    )

    with open(args.output, "w") as fp:
        fp.write(src)


def _make_type(name: str, members: list[str]) -> dict:
    fields = []
    for mem in members:
        type_name, field_name = mem.rsplit(" ", 1)
        fields.append({"type": type_name, "name": field_name})
    visit_method = name[0].lower() + name[1:]
    return {"name": name, "fields": fields, "visit_method": visit_method}


if __name__ == "__main__":
    entrypoint()
