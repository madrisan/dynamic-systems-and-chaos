#!/usr/bin/python3

# Plot the Bifurcation Diagram of Logistic, Cubic, and Sine Maps
# Copyright (C) 2016-2018 Davide Madrisan <davide.madrisan@gmail.com>
# SPDX-License-Identifier: Apache-2.0

import argparse
import sys
import textwrap

from lelib import Bifurcation, Map
from utils import copyleft, die

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
                 formatter_class = argparse.RawDescriptionHelpFormatter,
                 description = copyleft(descr),
                 epilog = "Examples:\n" + textwrap.dedent(examples))

    # By default, make 300 iterations (n) and do no plot the first 200 ones (s)
    # By default select the Logistic Equation

    parser.add_argument(
        "-r", "--rate",
        action="store", dest="r",
        help="range of the growth rate parameter (default: the entire range)")
    parser.add_argument(
        "-y", "--people",
        action="store", dest="y",
        help="normalized range of the population (default: the entire range)")
    parser.add_argument(
        "-s", "--skip",
        action="store", dest="s", type=int, default=200,
        help="skip plotting the first 's' iterations (default: %(default)s)")
    parser.add_argument(
        "-n", "--steps",
        action="store", dest="n", type=int, default=100,
        help="number of iterations (default: %(default)s)")
    parser.add_argument(
        "-m", "--map",
        action="store", dest="map_name", default="logistic",
        choices=["logistic", "cubic", "sine"],
        help="select the desired map (logistic, cubic, or sine)")

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
