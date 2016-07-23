#!/usr/bin/python2

# Logistic Equation: Comparing Initial Conditions
# Copyright (C) 2016 Davide Madrisan <davide.madrisan.gmail.com>

__author__ = "Davide Madrisan"
__copyright__ = "Copyright (C) 2016 Davide Madrisan"
__license__ = "GPL"
__version__ = "2"
__email__ = "davide.madrisan.gmail.com"
__status__ = "stable"

import getopt
import sys
import numpy as np
import matplotlib.pyplot as plt

class Logistic(object):
    """Class for plotting a Logistic Map rx(1-x) """

    def __init__(self, r, n, x0, dotsonly = False):
        self.r = r    # Grow rate parameter
        self.n = n    # Number of iterations
        self.x0 = x0  # The 1st initial condition

        self.x = self.y1 = []
        self.dotsonly = dotsonly

    def _plotline(self, x, y, color):
        """Plot the dots (x, y) connected by straight lines
           if the parameter 'dotsonly' if set to False """

        assert x.any() and y.any(), '_plotline(): internal error'

        plt.plot(x, y, color + 'o')
        if not self.dotsonly: plt.plot(x, y, color)

    def getxy(self):
        """Set the numpy vectors 'x' and 'y1' containing
           the iterations (1..n) and the corresponding values
           of the Logistic Equation rx(1-x) """

        # do not initialize twice the x and y1 vectors
        if len(self.x) > 0: return

        self.x = np.arange(self.n)

        self.y1 = np.arange(0, self.n, 1.)
        self.y1[0] = self.x0

        for t in self.x[1:]:
            self.y1[t] = self.r * self.y1[t-1] * (1 - self.y1[t-1])

        return self.x, self.y1

    def plot(self):
        """Plot a Logistic Equation map """

        color = 'g'

        self.getxy()

        plt.title('Logistic Equation')
        plt.xlabel('time t')
        plt.ylim([0, 1.])
        plt.grid(True)
        self._plotline(self.x, self.y1, color)

        plt.show()


class LogisticDiff(Logistic):
    """Derived class for plotting a Logistic Map rx(1-x)
       with two different initial conditions, followed by a plot of
       their differences (for a visualization of the Butterfly Effect) """

    def __init__(self, r, n, x0, x1, dotsonly = False):
        Logistic.__init__(self, r, n, x0, dotsonly)

        self.x1 = x1  # The 2st initial condition
        self.y2 = []

    def getxy(self):
        """Set the numpy vectors 'x', 'y1', and 'y2' containing
           the iterations (1..n) and the corresponding values
           of the Logistic Equation rx(1-x) """

        super(LogisticDiff, self).getxy()

        # do not initialize twice the vector y2
        if len(self.y2) > 0: return

        self.y2 = np.arange(0, self.n, 1.)
        self.y2[0] = self.x1

        for t in self.x[1:]:
            self.y2[t] = self.r * self.y2[t-1] * (1 - self.y2[t-1])

        return self.x, self.y1, self.y2

    def plot(self):
        """Plot a Logistic Equation map with two different seeds (two plots)
           followed by their difference """

        color = ['g', 'r']

        self.getxy()

        plt.figure(1)

        plt.subplot(211)
        plt.title('Time series for a logistic equation with two different initial conditions')
        plt.ylabel(r'$y_1(t),\ y_2(t)$', fontsize=14)
        plt.ylim([0, 1.])
        plt.grid(True)
        self._plotline(self.x, self.y1, color[0])
        self._plotline(self.x, self.y2, color[1])

        ydiff = self.y2 - self.y1

        plt.subplot(212)
        plt.title('Difference between the two time series')
        plt.xlabel('time t')
        plt.ylabel(r'$y_2(t) - y_1(t)$', fontsize=14)
        plt.grid(True)
        self._plotline(self.x, ydiff, 'b')

        plt.show()


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
        progname + ' --x0 <float> [--x1 <float>] [-d] -r <float> -n <int>\n' +
        progname + ' -h\n')

    writeln("""Where:
  -0 | --x0: 1st initial condition
  -1 | --x1: 2nd initial condition (optional)
  -d | --dots-only: do not connect the dots with lines
  -r | --rate: growth rate parameter
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
        opts, args = getopt.getopt(sys.argv[1:], '0:1:dn:r:h',
                   ["x0=", "x1=", "dots-only", "steps=", "rate=", "help"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    x0 = x1 = n = r = None
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
        else:
            assert False, "Unhandled command-line option"

    if not x0 or not n or not r:
        usage()
        die(2, 'One of more arguments have not been set.')

    le = LogisticDiff(r, n, x0, x1, dotsonly) if x1 \
             else Logistic(r, n, x0, dotsonly)
    le.plot()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        die(3, 'Exiting on user request')

    sys.exit()
