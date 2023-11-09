# author: Tiffany Timbers
# date: 2020-02-23

"""Calculates and prints the square root of a given number.
Usage: sqrt.py --n=<n>

Options:
--n=<n>    Number for which the square root should be calculated
"""

import math
from docopt import docopt

opt = docopt(__doc__)


def main(number):
    """
    Calculates and prints the square root of a number.
    """
    if number < 0:
        raise Exception("n should not a positive number")
    number = int(number)
    print(math.sqrt(number))


if __name__ == "__main__":
    main(opt["--n"])
