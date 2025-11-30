from typing import TYPE_CHECKING

from ._base import utility

if TYPE_CHECKING:
    from argparse import Namespace
    from io import TextIOWrapper


@utility(lambda r:
         r.add_argument("wraps", nargs=2, metavar="WRAPPER", action="append")
         and r.add_argument("--wrap", nargs=2, action="append", dest="wraps")
         )
def wrap(options: "Namespace", infile: "TextIOWrapper", outfile: "TextIOWrapper"):
    for line in infile:
        for wrap in options.wraps:
            outfile.write(f"{wrap[0]}{line.rstrip()}{wrap[1]}\n")


# noinspection PyUnusedLocal
@utility()
def single_quote(options: "Namespace", infile: "TextIOWrapper", outfile: "TextIOWrapper"):
    del options

    for line in infile:
        outfile.write(f"'{line.rstrip()}'\n")


# noinspection PyUnusedLocal
@utility()
def double_quote(options: "Namespace", infile: "TextIOWrapper", outfile: "TextIOWrapper"):
    del options

    for line in infile:
        outfile.write(f'"{line.rstrip()}"\n')
