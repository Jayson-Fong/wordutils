import html
from typing import TYPE_CHECKING

from ._base import utility

if TYPE_CHECKING:
    from argparse import Namespace
    from io import TextIOWrapper


# noinspection PyUnusedLocal
@utility()
def escape(options: "Namespace", infile: "TextIOWrapper", outfile: "TextIOWrapper"):
    del options

    for line in infile:
        outfile.write(f"{html.escape(line.rstrip())}\n")
