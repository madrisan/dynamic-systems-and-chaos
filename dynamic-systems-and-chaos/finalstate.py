#!/usr/bin/python3

# Final State Diagram
# Copyright (C) 2016-2018 Davide Madrisan <davide.madrisan@gmail.com>
# SPDX-License-Identifier: Apache-2.0

import argparse
import sys

from lelib import FinalState
from utils import argparser, copyleft, die

def parse_args():
    """This function parses and return arguments passed in """
    descr = 'Plot of the Final State Diagram'
    examples = '''
      %(prog)s -r 3.492
      %(prog)s -r 3.614 -s 200 -n 300
      %(prog)s -0 0.4 -r 3.2 -s 10 -n 50
      %(prog)s -0 0.8 -r 6.2 -n 20 --map=cubic'''

    parser = argparser(descr, examples)

    # By default, make 3000 iterations (n) and
    # do no plot the first 2000 ones (s)
    # By default select the Logistic Equation

    parser.add_argument(
        "-0", "--x0",
        action="store", dest="x0", type=float, default=.5,
        help="initial condition (default: %(default)s)")
    parser.add_argument(
        "-r", "--rate",
        action="store", dest="r", type=float, required=True,
        help="growth rate parameter")
    parser.add_argument(
        "-s", "--skip",
        action="store", dest="s", type=int, default=2000,
        help="skip plotting the first 's' iterations (default: %(default)s)")
    parser.add_argument(
        "-n", "--steps", dest="n", type=int, default=1000, action="store",
        help="number of iterations (default: %(default)s)")
    parser.add_argument(
        "-m", "--map",
        action="store", dest="map_name", default = "logistic",
        choices = ["logistic", "cubic", "sine"],
        help = "select the desired map (logistic, cubic, or sine)")

    return parser.parse_args()


def main():
    args = parse_args()

    FinalState(
        args.r,
        args.n,
        args.x0,
        args.s,
        args.map_name
    ).plot()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        die(3, 'Exiting on user request')

    sys.exit()
