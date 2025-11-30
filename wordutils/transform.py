from typing import TYPE_CHECKING

from ._base import utility

if TYPE_CHECKING:
    from argparse import Namespace
    from io import TextIOWrapper


# noinspection PyUnusedLocal
@utility()
def reverse(options: "Namespace", infile: "TextIOWrapper", outfile: "TextIOWrapper"):
    del options

    for line in infile:
        outfile.write(f"{line.rstrip()[::-1]}\n")


# noinspection PyUnusedLocal
@utility()
def upper(options: "Namespace", infile: "TextIOWrapper", outfile: "TextIOWrapper"):
    del options

    for line in infile:
        outfile.write(line.upper())


# noinspection PyUnusedLocal
@utility()
def lower(options: "Namespace", infile: "TextIOWrapper", outfile: "TextIOWrapper"):
    del options

    for line in infile:
        outfile.write(line.lower())


# noinspection PyUnusedLocal
# noinspection SpellCheckingInspection
@utility()
def swapcase(options: "Namespace", infile: "TextIOWrapper", outfile: "TextIOWrapper"):
    del options

    for line in infile:
        outfile.write(line.swapcase())


# noinspection PyUnusedLocal
@utility()
def capitalize(options: "Namespace", infile: "TextIOWrapper", outfile: "TextIOWrapper"):
    del options

    for line in infile:
        outfile.write(line.capitalize())


# noinspection PyUnusedLocal
@utility()
def title(options: "Namespace", infile: "TextIOWrapper", outfile: "TextIOWrapper"):
    del options

    for line in infile:
        outfile.write(line.title())
