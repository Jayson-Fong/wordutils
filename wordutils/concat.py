from typing import TYPE_CHECKING

from ._base import utility

if TYPE_CHECKING:
    from argparse import Namespace
    from io import TextIOWrapper


@utility(lambda r: r.add_argument("prefixes", nargs="+"))
def prefix(options: "Namespace", infile: "TextIOWrapper", outfile: "TextIOWrapper"):
    for line in infile:
        for prefix in options.prefixes:
            outfile.write(f"{prefix}{line}")


@utility(lambda r: r.add_argument("suffixes", nargs="+"))
def suffix(options: "Namespace", infile: "TextIOWrapper", outfile: "TextIOWrapper"):
    for line in infile:
        for suffix in options.suffixes:
            outfile.write(f"{line.rstrip()}{suffix}\n")
