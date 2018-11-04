#!/usr/bin/python3

# Logistic Equation: Comparing Initial Conditions
# Copyright (C) 2016-2018 Davide Madrisan <davide.madrisan@gmail.com>
# SPDX-License-Identifier: Apache-2.0

import getopt
import sys

from lelib import Logistic, LogisticDiff
from utils import copyleft, die, writeln

def usage():
    """Program usage """

    progname = '  ' + sys.argv[0]

    writeln('Usage:\n' +
        progname + ' --x0 <float> [--x1 <float>] [-d] -r <float> -n <int> ' \
            + '[-s <int>] [-c|-l|-t]\n' +
        progname + ' -h\n')

    writeln("""Where:
  -0 | --x0: 1st initial condition
  -1 | --x1: 2nd initial condition (optional)
  -d | --dots-only: do not connect the dots with lines
  -r | --rate: growth rate parameter
  -s | --skip: skip plotting the first 'k' iterations
  -n | --steps: number of iterations
  -c | --cubic: plot the bifurcation diagram of the cubic map
  -l | --logistic: plot the diagram of the logistic map (default)
  -t | --sine: plot the diagram of the sine map\n""")

    writeln('Example:\n' +
        '  # time series with a stable fixed point\n' +
        progname + ' -0 0.4 -r 3.2 -n 50\n' +
        progname + ' -0 0.4 -1 0.45 -r 3.2 -n 50\n\n' +
        '  # chaotic results (randon output)\n' +
        progname + ' --x0 0.2 --x1 0.2000001 -r 4.0 -n 50\n' +
        progname + ' -0 0.2 -r 3.6 -n 5000 --dots-only\n' +
        progname + ' -0 0.9 -r 4.5 -n 50 --cubic\n' +
        progname + ' -0 0.4 -r 0.8 -n 50 --sine\n')

def helpmsg():
    """Print the Copyright and an help message """

    descr = 'Plot of Logistic Equation Time Series'
    copyleft(descr)
    usage()

def main():
    try:
        opts, _ = getopt.getopt(sys.argv[1:], '0:1:dn:r:s:hclt',
            ["x0=", "x1=", "dots-only", "steps=", \
             "rate=", "skip=", "help", "cubic", "logistic", "sine"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    x0 = x1 = n = r = None
    s = 0
    dotsonly = False
    # By default select the Logistic Equation
    map_name = 'logistic'

    for o, a in opts:
        if o in ('-h', '--help'):
            helpmsg()
            sys.exit()
        elif o in ('-0', '--x0'):
            x0 = float(a)
        elif o in ('-1', '--x1'):
            x1 = float(a)
        elif o in ('-d', '--dots-only'):
            dotsonly = True
        elif o in ('-n', '--steps'):
            n = int(a)
        elif o in ('-r', '--rate'):
            r = float(a)
        elif o in ('-s', '--skip'):
            s = int(a)
        elif o in ('-c', '--cubic'):
            map_name = 'cubic'
        elif o in ('-l', '--logistic'):
            map_name = 'logistic'
        elif o in ('-t', '--sine'):
            map_name = 'sine'
        else:
            raise AssertionError("Unhandled command-line option.")

    if x0 == None or n == None or r == None:
        usage()
        die(2, 'One of more arguments have not been set.')

    lemap = LogisticDiff(r, n, x0, x1, s, dotsonly, map_name) if x1 \
                else Logistic(r, n, x0, s, dotsonly, map_name)
    lemap.plot()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        die(3, 'Exiting on user request')

    sys.exit()
