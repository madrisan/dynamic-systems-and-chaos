#!/usr/bin/python3

# Logistic Equation: Comparing Initial Conditions
# Copyright (C) 2016-2018 Davide Madrisan <davide.madrisan@gmail.com>
# SPDX-License-Identifier: Apache-2.0

import argparse
import sys

from lelib import Logistic, LogisticDiff
from utils import argparser, copyleft, die

def parse_args():
    """This function parses and return arguments passed in """
    descr = 'Plot of Logistic Equation Time Series'
    examples = '''
      # time series with a stable fixed point
      %(prog)s -0 0.4 -r 3.2 -n 50
      %(prog)s -0 0.4 -1 0.45 -r 3.2 -n 50
      # chaotic results (randon output)
      %(prog)s --x0 0.2 --x1 0.2000001 -r 4.0 -n 50
      %(prog)s -0 0.2 -r 3.6 -n 5000 --dots-only
      %(prog)s -0 0.9 -r 4.5 -n 50 --map=cubic
      %(prog)s -0 0.4 -r 0.8 -n 50 --map=sine'''

    parser = argparser(descr, examples)

    # By default select the Logistic Equation

    parser.add_argument(
        "-0", "--x0",
        action="store", dest="x0", type=float, required=True,
        help="1st initial condition")
    parser.add_argument(
        "-1", "--x1",
        action="store", dest="x1", type=float,
        help="2nd initial condition (optional)")
    parser.add_argument(
        "-d", "--dots-only",
        action="store", dest="dotsonly", type=bool, default=False,
        help="do not connect the dots with lines (default: %(default)s)")
    parser.add_argument(
        "-r", "--rate",
        action="store", dest="r", type=float, required=True,
        help="growth rate parameter")
    parser.add_argument(
        "-s", "--skip",
        action="store", dest="s", type=int, default=0,
        help="skip plotting the first 's' iterations")
    parser.add_argument(
        "-n", "--steps",
        action="store", dest="n", type=int, required=True,
        help="number of iterations")
    parser.add_argument(
        "-m", "--map",
        action="store", dest="map_name", default="logistic",
        choices = ["logistic", "cubic", "sine"],
        help = "select the desired map (logistic, cubic, or sine)")

    return parser.parse_args()

def main():
    args = parse_args()

    lemap = (
        LogisticDiff(
            args.r, args.n, args.x0, args.x1, args.s, args.map_name)
        if args.x1 else Logistic(
            args.r, args.n, args.x0, args.s, args.map_name))

    lemap.plotdots = not args.dotsonly
    lemap.plot()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        die(3, 'Exiting on user request')

    sys.exit()
