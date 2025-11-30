import argparse
import sys
from contextlib import contextmanager


@contextmanager
def open_file(filename, read: bool = True, encoding: str = "utf-8"):
    if filename == "-":
        if read:
            if sys.stdin.isatty():
                sys.exit("Cannot read from stdin with attached terminal.")

            yield sys.stdin
        else:
            yield sys.stdout

        return

    with open(filename, "r" if read else "w", encoding=encoding) as f:
        yield f


def utility(registrar=None):
    def applicator(func):
        def wrapper(args=None):
            parser = argparse.ArgumentParser()
            parser.add_argument("--input", "-i", "-r", default="-")
            parser.add_argument("--output", "-o", "-w", default="-")

            if registrar:
                registrar(parser)

            p_args = parser.parse_args(args)
            with open_file(p_args.input) as i, open_file(p_args.output, read=False) as o:
                return func(p_args, i, o)

        return wrapper

    return applicator
