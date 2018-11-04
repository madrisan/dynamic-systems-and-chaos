#!/usr/bin/python3

# Logistic Equation Library
# Copyright (C) 2016-2018 Davide Madrisan <davide.madrisan@gmail.com>

__author__ = "Davide Madrisan"
__copyright__ = "Copyright (C) 2016-2018 Davide Madrisan"
__license__ = "Apache License 2.0"
__version__ = "3"
__email__ = "davide.madrisan@gmail.com"
__status__ = "stable"

import sys
import numpy as np
import matplotlib.pyplot as plt
from math import pi, sin

class Map(object):
    """Class that provides the map functions along with r and y ranges """

    def __init__(self, mapname='logistic'):
        params = {
                      # rmin rmax ymin ymax function
            'cubic'   : [ 0, 6.5, 0, 1, lambda r, x: r * x**2 * (1.0 - x)  ],
            'logistic': [ 0, 4.0, 0, 1, lambda r, x: r * x * (1.0 - x)     ],
            'sine'    : [ 0, 2.0, 0, 2, lambda r, x: r * sin(pi * x / 2.0) ]
        }

        self.map_name = mapname
        self.map_longname = "%s Equation" % mapname.capitalize()

        try:
            self.map_rmin, self.map_rmax, \
            self.map_ymin, self.map_ymax, \
            self.map_function = params[mapname]
            self.map = self._mapper
        except Exception as e:
            raise type(e)('Unknown map name ' + mapname)

    @staticmethod
    def ensure(expression, message, *argv):
        if not expression:
            raise AssertionError(message % (argv) if argv else message)

    def _mapper(self, r, x):
        self.ensure(
            (r >= self.map_rmin and r <= self.map_rmax),
            'The growth parameter r must be between %g and %g',
            self.map_rmin, self.map_rmax)
        return self.map_function(r, x)

class Logistic(Map):
    """Class for plotting a Logistic/Cubic/Sine Map """

    def __init__(self, r, n, x0, s=0, dotsonly=False, mapname='logistic'):
        Map.__init__(self, mapname)

        self.r = r    # Growth rate parameter

        self.ensure(n > 0,
                    'The number of iterations must be greater than zero.')
        self.n = n    # Number of iterations

        self.ensure(s >= 0,
                    'You cannot skip a negative number of iterations.')
        self.s = s    # Number of iterations to skip in the plot

        self.ensure(x0 >= self.map_ymin and x0 <= self.map_ymax,
                    'The initial condition x0 should be in [%g, %g].',
                    self.map_ymin, self.map_ymax)
        self.x0 = x0  # The 1st initial condition

        self.x = self.y1 = []
        self.dotsonly = dotsonly

    def _plotline(self, x, y, color):
        """Plot the dots (x, y) connected by straight lines
           if the parameter 'dotsonly' if set to False """

        self.ensure(x.any() and y.any(), '_plotline(): internal error')
        plt.plot(x, y, color=color, linestyle='',
                 markerfacecolor=color, marker='o', markersize=8)
        if not self.dotsonly: plt.plot(x, y, color=color, alpha=0.6)

    def getxy(self):
        """Set the numpy vectors 'x' and 'y1' containing
           the iterations (1..n) and the corresponding values
           of the choosen Map """

        # do not initialize twice the x and y1 vectors
        if len(self.x) > 0: return

        vectlen = self.n + self.s + 1

        self.x = np.arange(vectlen)
        self.y1 = np.arange(0, vectlen, 1.)
        self.y1[0] = self.x0

        for t in self.x[1:]:
            self.y1[t] = self.map(self.r, self.y1[t-1])

        return self.x, self.y1

    def plot(self):
        """Plot a Logistic, Cubic or Sine map """

        self.getxy()

        plt.suptitle('Dynamic Systems and Chaos', fontsize=14, fontweight='bold')
        plt.title(self.map_longname)
        plt.xlabel('time t')
        plt.ylim([self.map_ymin, self.map_ymax])
        plt.grid(True)
        self._plotline(self.x[self.s:], self.y1[self.s:], 'mediumseagreen')

        plt.show()


class FinalState(Logistic):
    """Derived class for plotting a Final State Diagram """

    # By default, set the initial state to .5
    # make 3000 iterations and do no plot the first 2000 ones
    def __init__(self, r, n=1000, x0=.5, s=2000, mapname='logistic'):
        Logistic.__init__(self, r, n, x0, s, True, mapname)

    def getxy(self, y=.5):
        """Set the numpy vectors 'x' and 'y1' containing the values of the
           choosen Map for the first n iterations """

        # do not initialize twice the x and y1 vectors
        if len(self.x) > 0: return

        vectlen = self.n + self.s + 1

        self.y1 = np.full(vectlen, y, dtype=np.float)
        self.x = np.full(vectlen, self.x0, dtype=np.float64)

        for t in range(1, vectlen):
            self.x[t] = self.map(self.r, self.x[t-1])

        return self.x, self.y1

    def plot(self):
        """Plot a Final State Diagram """

        self.getxy()

        plt.suptitle('Dynamic Systems and Chaos', fontsize=14, fontweight='bold')
        plt.title('Final State Diagram for the ' + self.map_longname)

        plt.xlim([self.map_ymin, self.map_ymax])
        plt.ylim([0, 1.])
        plt.yticks([])

        plt.grid(True)

        plt.plot([self.map_ymin, self.map_ymax], [.5, .5],
                 color='black', lw=1)
        plt.plot(self.x[self.s:], self.y1[self.s:], color='black', linestyle='',
                 markerfacecolor='black', marker='o', markersize=8)
        plt.text(.1 * self.map_ymax, .4, 'r = %g' % self.r, style='italic',
                 bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})

        plt.show()


class LogisticDiff(Logistic):
    """Derived class for plotting a Logistic/Cubic/Sine Map
       with two different initial conditions, followed by a plot of
       their differences (for a visualization of the Butterfly Effect) """

    def __init__(self, r, n, x0, x1, s=0, dotsonly=False, mapname='logistic'):
        Logistic.__init__(self, r, n, x0, s, dotsonly, mapname)

        self.ensure(x1 >= self.map_ymin and x1 <= self.map_ymax,
                    'The initial condition x1 should be in [%g, %g].',
                    self.map_ymin, self.map_ymax)
        self.x1 = x1  # The 2st initial condition
        self.y2 = []

    def getxy(self):
        """Set the numpy vectors 'x', 'y1', and 'y2' containing
           the iterations (1..n) and the corresponding values
           of the choosen Map """

        super(LogisticDiff, self).getxy()

        # do not initialize twice the vector y2
        if len(self.y2) > 0: return

        self.y2 = np.arange(0, self.n + self.s + 1, 1.)
        self.y2[0] = self.x1

        for t in self.x[1:]:
            self.y2[t] = self.map(self.r, self.y2[t-1])

        return self.x, self.y1, self.y2

    def getdiffy(self):
        """Return the difference between the two vectors y2 and y1 """

        return self.y2 - self.y1

    def plot(self):
        """Plot a Logistic, Cubic or Sine map with two different seeds (two plots)
           followed by their difference """

        self.getxy()

        plt.figure(1)
        plt.suptitle('Dynamic Systems and Chaos',
                     fontsize=14, fontweight='bold')

        plt.subplot(211)
        plt.title('Time series for a ' + self.map_longname + \
                  ' with two different initial conditions')
        plt.ylabel(r'$y_1(t),\ y_2(t)$', fontsize=14)
        plt.ylim([self.map_ymin, self.map_ymax])
        plt.grid(True)
        self._plotline(self.x[self.s:], self.y1[self.s:], 'indianred')
        self._plotline(self.x[self.s:], self.y2[self.s:], 'mediumseagreen')

        ydiff = self.y2 - self.y1

        plt.subplot(212)
        plt.title('Difference between the two time series')
        plt.xlabel('time t')
        plt.ylabel(r'$y_2(t) - y_1(t)$', fontsize=14)
        plt.grid(True)
        self._plotline(self.x[self.s:], ydiff[self.s:], 'royalblue')

        plt.show()


class Bifurcation(Map):
    """Class for plotting a Logistic/Cubic/Sine Bifurcation Diagram """
    def __init__(self, r, y, n=100, s=200, mapname='logistic'):
        Map.__init__(self, mapname)

        self.ensure(len(r) == 2, 'The growth rate vector should contains two elements')
        self.ensure(r[0] >= self.map_rmin and r[0] < r[1] and r[1] <= self.map_rmax,
                    ('The parameters [r0, r1] must be between %g and %g, '
                     'and in ascending order.'), self.map_rmin, self.map_rmax)
        self.ensure(len(y) == 2, 'The y range vector should contains two elements')
        self.ensure(y[0] >= self.map_ymin and y[0] < y[1] and y[1] <= self.map_ymax,
                    ('The parameters [y0, y1] must be between %g and %g, '
                     'and in ascending order.'), self.map_ymin, self.map_ymax)

        self.rmin = r[0]    # Range of the growth rate for plot()
        self.rmax = r[1]
        self.ymin = y[0]    # Range of the population for plot()
        self.ymax = y[1]

        self.ensure(n > 0, 'The number of iterations must be greater than zero.')
        self.n = n    # Number of iterations

        self.ensure(s >= 0, 'You cannot skip a negative number of iterations.')
        self.s = s    # Number of iterations to skip in the plot

    def plot(self):
        plt.suptitle('Dynamic Systems and Chaos', fontsize=14, fontweight='bold')
        plt.title('Bifurcation Diagram for the ' + self.map_longname)

        plt.xlim([self.rmin, self.rmax])
        plt.xticks([round(i, 1) for i in np.linspace(self.rmin, self.rmax, 5)])
        plt.xlabel('r')

        plt.ylim([self.ymin, self.ymax])
        plt.ylabel('final states')

        for r in np.linspace(self.rmin, self.rmax, 1000):
            x, y = FinalState(r, self.n, .5, self.s, self.map_name).getxy(r)
            plt.plot(y[self.s:], x[self.s:], color='black', linestyle='',
                     markerfacecolor='black', marker=',', markersize=1)

        plt.show()


def test_class_map():
    """Test the class 'Map' """
    sys.stdout.write("Running the tests for the class 'Map'...\n")
    m = Map()
    m.ensure(m.map_name == 'logistic', "The default map should be 'logistic'")
    m.ensure(m.map_longname == 'Logistic Equation',
             "Logistic Map: bad long name")
    m.ensure(m.map_rmin == 0 and m.map_rmax == 4,
             "Logistic Map: bad range for r")
    m.ensure(m.map_ymin == 0 and m.map_ymax == 1,
             "Logistic Map: bad range for y")
    i = m.map(4,.25)
    m.ensure(i == .75,
             "Logistic Map: bad value for r=4 and x=.25: should be %f" % i)

    m = Map('cubic')
    m.ensure(m.map_name == 'cubic', "Cubic Map: bad map selection")
    m.ensure(m.map_longname == 'Cubic Equation', "Cubic Map: bad long name")
    m.ensure(m.map_rmin == 0 and m.map_rmax == 6.5,
             "Cubic Map: bad range for r")
    m.ensure(m.map_ymin == 0 and m.map_ymax == 1,
             "Cubic Map: bad range for y")
    i = m.map(2,.5)
    m.ensure(i == .25,
             "Cubic Map: bad value for r=2 and x=.5, should be %f" % i)

    m = Map('sine')
    m.ensure(m.map_name == 'sine', "Sine Map: bad map selection")
    m.ensure(m.map_longname == 'Sine Equation', "Sine Map: bad long name")
    m.ensure(m.map_rmin == 0 and m.map_rmax == 2, "Sine Map: bad range for r")
    m.ensure(m.map_ymin == 0 and m.map_ymax == 2, "Sine Map: bad range for y")
    i = m.map(0.5,1)
    m.ensure(i == .5,
             "Sine Map: bad value for r=0.5 and x=1: should be %f" % i)

def test_class_logistic():
   """Test the class 'Logistic' """
   sys.stdout.write("Running the tests for the class 'Logistic'...\n")
   r, n, x0 = 3.2, 100, 0.4
   le1 = Logistic(r, n, x0, False, 'logistic')
   x, y1 = le1.getxy()

   m = Map()
   m.ensure(len(x) == n+1, "x should be a vector of size %d" % (n+1))
   m.ensure(x[0] == 0, "x[0] should be 0")
   m.ensure(x[n] == n, "the last element of x should be equal to %d" % n)
   m.ensure(x.sum() == n*(n+1)/2,
            "the sum of the elements of x is not correct")

   m.ensure(len(y1) == n+1, "y1 should be a vector of size %d" % (n+1))
   m.ensure(y1[0] == x0, "the first element of y1 should be equal to x0")
   m.ensure(y1[n] == y1[n-2], "y1 is expected to be periodic with period 2")
   m.ensure(y1[n-1] == y1[n-3], "y1 is expected to be periodic with period 2")

def test_class_logisticdiff():
   """Test the class 'LogisticDiff' """
   sys.stdout.write("Running the tests for the class 'LogisticDiff'...\n")
   r, n, x0, x1 = 4.0, 50, 0.2, 0.2000001
   le2 = LogisticDiff(r, n, x0, x1, False, 'logistic')
   x, y1, _ = le2.getxy()

   m = Map()
   m.ensure(len(x) == n+1, "x should be a vector of size %d" % (n+1))
   m.ensure(x[0] == 0, "x[0] should be 0")
   m.ensure(x[n] == n, "the last element of x should be equal to %d" % n)
   m.ensure(x.sum() == n*(n+1)/2,
            "the sum of the elements of x is not correct")

   m.ensure(len(y1) == n+1, "y1 should be a vector of size %d" % (n+1))
   m.ensure(y1[0] == x0, "the first element of y1 should be equal to x0")

   ydiff = le2.getdiffy()
   m.ensure(len(ydiff) == n+1,
            "the vector y2-y1 should have a size equal to %d" % (n+1))
   m.ensure(np.all(ydiff < 1e3) and np.all(ydiff > -1e3),
            "the diff vector should show the Butterfly Effect")

if __name__ == '__main__':
    test_class_map()
    test_class_logistic()
    test_class_logisticdiff()

    sys.stdout.write("All tests successfully passed!\n")
