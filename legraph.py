#!/usr/bin/python2

# Logistic Equation: Comparing Initial Conditions
# Copyright (C) 2016 Davide Madrisan <davide.madrisan.gmail.com>

__author__ = "Davide Madrisan"
__copyright__ = "Copyright 2016 Davide Madrisan"
__license__ = "GPL"
__version__ = "1"
__email__ = "davide.madrisan.gmail.com"
__status__ = "stable"

import getopt
import sys
import numpy as np
import matplotlib.pyplot as plt

# r : Parameter
# n : Number of Iterations
# x0: Initial condition
def logistic(r, n, x0):
    x = np.arange(n)
    y = np.arange(0, n, 1.0)

    y[0] = x0
    for t in x[1:]:
        y[t] = r * y[t-1] * (1 - y[t-1])

    return x, y

def plotline(x, y, color):
    plt.plot(x, y, color + 'o', x, y, color)

def plotsingle(x, y, color):
    plt.title('Logistic Equation')
    plt.xlabel('time t')
    plt.ylim([0, 1.0])
    plt.grid(True)
    plotline(x, y, color)

def plotwithdiff(x, y1, y2, color):
    plt.figure(1)

    plt.subplot(211)
    plt.title('Time series for a logistic equation with two different initial conditions')
    plt.ylabel(r'$y_1(t),\ y_2(t)$', fontsize=14)
    plt.ylim([0, 1.0])
    plt.grid(True)
    plotline(x, y1, color[0])
    plotline(x, y2, color[1])

    ydiff = y2 - y1

    plt.subplot(212)
    plt.title('Difference between the two time series')
    plt.xlabel('time t')
    plt.ylabel(r'$y_2(t) - y_1(t)$', fontsize=14)
    plt.grid(True)
    plotline(x, ydiff, 'b')

def die(exitcode, message):
    "Print error and exit with the requested errorcode"
    progname = sys.argv[0]
    sys.stderr.write('%s: error: %s\n' % (progname, message))
    sys.exit(exitcode)

def writeln(line):
    sys.stdout.write(line + '\n')

def usage():
    progname = sys.argv[0]
    writeln('Usage:\n' +
        progname + ' -x0 <1st-init-cond> [-x1 <2nd-init-cond>] -r <growth-rate> -n <steps>\n' +
        progname + ' -h\n')
    writeln('Example:\n' +
        '# of a time series with a stable fixed point\n' +
        progname + ' --x0 0.4 -r 3.2 -n 50\n' +
        progname + ' --x0 0.4 --x1 0.45 -r 3.2 -n 50\n' +
        '# of a chaotic result (randon output)\n' +
        progname + ' --x0 0.2 --x1 0.2000001 -r 4.0 -n 50\n')

def proghelp():
    writeln('Plot of Logistic Equation Time Series\n' +
            'Copyright (C) 2016 Davide Madrisan <davide.madrisan.gmail.com>\n')
    usage()

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], '0:1:n:r:h',
                   ["x0=", "x1=", "steps=", "rate=", "help"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    x0 = x1 = n = r = None

    for o, a in opts:
        if o in ('-h', '--help'):
            proghelp()
            sys.exit()
        elif o in ('-0', '--x0'):
            x0 = float(a)
        elif o in ('-1', '--x1'):
            x1 = float(a)
        elif o in ('-n', '--steps'):
            n = int(a)
        elif o in ('-r', '--rate'):
            r = float(a)
        else:
            assert False, 'unhandled command-line option'

    if not x0 or not n or not r:
        usage()
        die(2, 'one of more arguments have not been set.')

    t, y1 = logistic(r, n, x0)

    if x1:
        t, y2 = logistic(r, n, x1)
        plotwithdiff(t, y1, y2, ['g', 'r'])
    else:
        plotsingle(t, y1, 'g')

    plt.show()

if __name__ == '__main__':
    exitcode = 0
    try:
        main()
    except KeyboardInterrupt:
        die(3, 'Exiting on user request')
    sys.exit(exitcode)
