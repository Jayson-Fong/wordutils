from typing import TYPE_CHECKING

from ._base import utility

if TYPE_CHECKING:
    from argparse import Namespace
    from io import TextIOWrapper


# noinspection PyUnusedLocal
@utility()
def blank(options: "Namespace", infile: "TextIOWrapper", outfile: "TextIOWrapper"):
    del options

    for line in infile:
        if not line.strip():
            outfile.write(line)


# noinspection PyUnusedLocal
@utility()
def nonblank(options: "Namespace", infile: "TextIOWrapper", outfile: "TextIOWrapper"):
    del options

    for line in infile:
        if line.strip():
            outfile.write(line)


# noinspection PyUnusedLocal
@utility()
def title(options: "Namespace", infile: "TextIOWrapper", outfile: "TextIOWrapper"):
    del options

    for line in infile:
        if line.istitle():
            outfile.write(line)


# noinspection PyUnusedLocal
@utility()
def nontitle(options: "Namespace", infile: "TextIOWrapper", outfile: "TextIOWrapper"):
    del options

    for line in infile:
        if not line.istitle():
            outfile.write(line)
