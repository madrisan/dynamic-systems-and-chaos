#!/usr/bin/python3

# Plot the Bifurcation Diagram of Logistic, Cubic, and Sine Maps
# Copyright (C) 2016-2018 Davide Madrisan <davide.madrisan@gmail.com>
# SPDX-License-Identifier: Apache-2.0

import argparse
import getopt
import os
import sys
import textwrap

from lelib import Bifurcation, Map
from utils import copyleft

def parse_args():
    """This function parses and return arguments passed in """
    descr = 'Plot the Bifurcation Diagram of Logistic, Cubic, and Sine Maps'
    examples = '''
      %(prog)s -r 1:4
      %(prog)s -r 4:6.5 --map=cubic
      %(prog)s --map=sine -s 200 -n 200
      %(prog)s -r 3.:4. -s 500 -n 600
      %(prog)s -r 3.5:3.6 -y .3:.6 -s 800 -n 1000'''

    parser = argparse.ArgumentParser(
                 prog = os.path.basename(sys.argv[0]),
                 formatter_class = argparse.RawDescriptionHelpFormatter,
                 description = copyleft(descr),
                 epilog = "Examples:\n" + textwrap.dedent(examples))

    # By default, make 300 iterations (n) and do no plot the first 200 ones (s)
    # By default select the Logistic Equation

    parser.add_argument(
        "-r", "--rate",
        action = "store",
        help = "range of the growth rate parameter (default: the entire range)",
        dest = "r")
    parser.add_argument(
        "-y", "--people",
        action = "store",
        help = "normalized range of the population (default: the entire range)",
        dest = "y")
    parser.add_argument(
        "-s", "--skip",
        action = "store",
        default = 200,
        type = int,
        help = "skip plotting the first 's' iterations (default: %(default)s)",
        dest = "s")
    parser.add_argument(
        "-n", "--steps",
        action = "store",
        default = 100,
        type = int,
        help = "number of iterations (default: %(default)s)",
        dest = "n")
    parser.add_argument(
        "-m", "--map",
        action = "store",
        choices = ["logistic", "cubic", "sine"],
        default = "logistic",
        help = "select the desired map (logistic, cubic, or sine)",
        dest = "map_name")

    return parser.parse_args()


def main():
    args = parse_args()
    mapobj = Map(args.map_name)

    # range to vector: "1:4" --> [1., 4.]
    r2v = (lambda a, minval, maxval :
             [float(i) for i in a.split(':')] if a else
             [minval, maxval])

    # Plot the entire diagram by default
    Bifurcation(
        r2v(args.r, mapobj.map_rmin, mapobj.map_rmax),
        r2v(args.y, mapobj.map_ymin, mapobj.map_ymax),
        args.n,
        args.s,
        args.map_name
    ).plot()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        die(3, 'Exiting on user request')

    sys.exit()
