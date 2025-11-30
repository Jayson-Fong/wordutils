from typing import TYPE_CHECKING

from ._base import utility

if TYPE_CHECKING:
    from argparse import Namespace
    from io import TextIOWrapper


# noinspection PyUnusedLocal
@utility()
def strip(options: "Namespace", infile: "TextIOWrapper", outfile: "TextIOWrapper"):
    del options

    for line in infile:
        outfile.write(f"{line.strip()}\n")


# noinspection PyUnusedLocal
# noinspection SpellCheckingInspection
@utility()
def lstrip(options: "Namespace", infile: "TextIOWrapper", outfile: "TextIOWrapper"):
    del options

    for line in infile:
        outfile.write(f"{line.lstrip()}\n")


# noinspection PyUnusedLocal
# noinspection SpellCheckingInspection
@utility()
def rstrip(options: "Namespace", infile: "TextIOWrapper", outfile: "TextIOWrapper"):
    del options

    for line in infile:
        outfile.write(f"{line.rstrip()}\n")

