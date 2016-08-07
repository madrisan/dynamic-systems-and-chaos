#!/usr/bin/python2

# Logistic Equation: Comparing Initial Conditions
# Copyright (C) 2016 Davide Madrisan <davide.madrisan@gmail.com>

__author__ = "Davide Madrisan"
__copyright__ = "Copyright (C) 2016 Davide Madrisan"
__license__ = "Apache License 2.0"
__version__ = "2"
__email__ = "davide.madrisan@gmail.com"
__status__ = "stable"

import getopt
import sys

from lelib import Logistic
from lelib import LogisticDiff

def die(exitcode, message):
    """Print and error message and exit with 'exitcode' """

    progname = sys.argv[0]
    sys.stderr.write('%s: error: %s\n' % (progname, message))
    sys.exit(exitcode)


def writeln(line):
    """Print the given line to stdout followed by a newline """

    sys.stdout.write(line + '\n')


def usage():
    """Program usage """

    progname = '  ' + sys.argv[0]

    writeln('Usage:\n' +
        progname + \
         ' --x0 <float> [--x1 <float>] [-d] -r <float> -n <int> [-s <int>]\n' +
        progname + ' -h\n')

    writeln("""Where:
  -0 | --x0: 1st initial condition
  -1 | --x1: 2nd initial condition (optional)
  -d | --dots-only: do not connect the dots with lines
  -r | --rate: growth rate parameter
  -s | --skip: skip plotting the first 's' iterations
  -n | --steps: number of iterations\n""")

    writeln('Example:\n' +
        '  # time series with a stable fixed point\n' +
        progname + ' -0 0.4 -r 3.2 -n 50\n' +
        progname + ' -0 0.4 -1 0.45 -r 3.2 -n 50\n\n' +
        '  # chaotic results (randon output)\n' +
        progname + ' --x0 0.2 --x1 0.2000001 -r 4.0 -n 50\n' +
        progname + ' -0 0.2 -r 3.6 -n 5000 --dots-only\n')


def help():
    """Print the Copyright and an help message """

    writeln('Plot of Logistic Equation Time Series v.' +
        __version__ + ' (' + __status__ +  ')')
    writeln(__copyright__ + ' <' + __email__ + '>\n')
    usage()


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], '0:1:dn:r:s:h',
            ["x0=", "x1=", "dots-only", "steps=", \
             "rate=", "skip=", "help"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    x0 = x1 = n = r = None
    s = 0
    dotsonly = False

    for o, a in opts:
        if o in ('-h', '--help'):
            help()
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
        else:
            assert False, "Unhandled command-line option."

    if x0 == None or n == None or r == None:
        usage()
        die(2, 'One of more arguments have not been set.')

    lemap = LogisticDiff(r, n, x0, x1, s, dotsonly) if x1 \
                else Logistic(r, n, x0, s, dotsonly)
    lemap.plot()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        die(3, 'Exiting on user request')

    sys.exit()
