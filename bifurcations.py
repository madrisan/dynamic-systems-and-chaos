#!/usr/bin/python2

# Plot the Bifurcation Diagram of the Logistic Equation
# Copyright (C) 2016 Davide Madrisan <davide.madrisan.gmail.com>

__author__ = "Davide Madrisan"
__copyright__ = "Copyright (C) 2016 Davide Madrisan"
__license__ = "Apache License 2.0"
__version__ = "1"
__email__ = "davide.madrisan.gmail.com"
__status__ = "beta"

import getopt
import sys

from lelib import Bifurcation

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
         ' [-r <float>:<float>] [-n <int>] [-s <int>]\n' +
        progname + ' -h\n')

    writeln("""Where:
  -r | --rate: range of the growth rate parameters (default: [0:4])
  -s | --skip: skip plotting the first 's' iterations (default: 200)
  -n | --steps: number of iterations (default: 100)\n""")

    writeln('Example:\n' +
        '  # time series with a stable fixed point\n' +
        progname + ' -r 0:4\n' +
        progname + ' -r 3.0:3.5 -s 2000 -n 1000\n')

def help():
    """Print the Copyright and an help message """

    writeln('Plot the Bifurcation Diagram of a Logistic Equation v.' +
        __version__ + ' (' + __status__ +  ')')
    writeln(__copyright__ + ' <' + __email__ + '>\n')
    usage()


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'n:r:s:h',
            ["steps=", "rate=", "skip=", "help"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    r = None
    # By default, make 3000 iterations and do no plot the first 2000 ones
    n = 100
    s = 200

    for o, a in opts:
        if o in ('-h', '--help'):
            help()
            sys.exit()
        elif o in ('-n', '--steps'):
            n = int(a)
        elif o in ('-r', '--rate'):
            r = [ float(i) for i in a.split(':')]
        elif o in ('-s', '--skip'):
            s = int(a)
        else:
            assert False, "Unhandled command-line option."

    if r == None:
        usage()
        die(2, 'You must set at least the growth rate parameter.')

    Bifurcation(r, n, s).plot()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        die(3, 'Exiting on user request')

    sys.exit()
