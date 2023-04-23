"""Top-level package for IrrigaMe."""
import sys
import click
from .irrigame import main

__author__ = """Alessandro Corradi"""
__email__ = 'tomacastagna98@gmail.com'
__version__ = '0.1.0'

"""Console script for irrigame."""

@click.command()
def main_command(args=None):
    main()
    return 0


if __name__ == "__main__":
    sys.exit(main_command())  # pragma: no cover
