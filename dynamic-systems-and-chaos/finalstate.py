#!/usr/bin/python3

# Final State Diagram
# Copyright (C) 2016,2017 Davide Madrisan <davide.madrisan@gmail.com>

__author__ = "Davide Madrisan"
__copyright__ = "Copyright (C) 2016,2017 Davide Madrisan"
__license__ = "Apache License 2.0"
__version__ = "2"
__email__ = "davide.madrisan@gmail.com"
__status__ = "stable"

import getopt
import sys

from lelib import FinalState

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
         ' [--x0 <float>] -r <float> [-n <int>] [-s <int>] [-c|-l|-t]\n' +
        progname + ' -h\n')

    writeln("""Where:
  -0 | --x0: initial condition (default: .5)
  -r | --rate: growth rate parameter
  -s | --skip: skip plotting the first 's' iterations (default: 2000)
  -n | --steps: number of iterations (default: 1000)
  -c | --cubic: plot the bifurcation diagram of the cubic map
  -l | --logistic: plot the diagram of the logistic map (default)
  -t | --sine: plot the diagram of the sine map\n""")

    writeln('Example:\n' +
        progname + ' -r 3.492\n' +
        progname + ' -r 3.614 -s 200 -n 300\n' +
        progname + ' -0 0.4 -r 3.2 -s 10 -n 50\n' +
        progname + ' -0 0.8 -r 6.2 -n 20 --cubic\n')

def helpmsg():
    """Print the Copyright and an help message """

    writeln('Plot of the Final State Diagram v.' +
        __version__ + ' (' + __status__ +  ')')
    writeln(__copyright__ + ' <' + __email__ + '>\n')
    usage()


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], '0:n:r:s:hclt',
            ["x0=", "steps=", "rate=", "skip=", "help",\
             "cubic", "logistic", "sine"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    r = None
    # By default, set to .5 the initial state
    x0 = .5
    # By default, make 3000 iterations but do no plot the first 2000 ones
    n = 1000
    s = 2000

    # By default select the Logistic Equation
    map_name = 'logistic'

    for o, a in opts:
        if o in ('-h', '--help'):
            helpmsg()
            sys.exit()
        elif o in ('-0', '--x0'):
            x0 = float(a)
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
            assert False, "Unhandled command-line option."

    if r == None:
        usage()
        die(2, 'You must set at least the growth rate parameter.')

    FinalState(r, n, x0, s, map_name).plot()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        die(3, 'Exiting on user request')

    sys.exit()
