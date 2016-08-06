#!/usr/bin/python

# Logistic Equation Library
# Copyright (C) 2016 Davide Madrisan <davide.madrisan@gmail.com>

__author__ = "Davide Madrisan"
__copyright__ = "Copyright (C) 2016 Davide Madrisan"
__license__ = "Apache License 2.0"
__version__ = "2"
__email__ = "davide.madrisan@gmail.com"
__status__ = "stable"

import sys
import numpy as np
import matplotlib.pyplot as plt

class Map(object):
    def __init__(self, map='logistic'):
        self.map = None
        if map == 'logistic':
            self.map = self._logistic
            self.map_description = 'Logistic Equation'
            self.map_rmin = 0
            self.map_rmax = 4.0

        assert self.map != None, 'Undefined or unknown map'

    def _logistic(self, r, x):
        """Logistic map: rx(1-x) """
        assert r >= self.map_rmin and r <= self.map_rmax, \
            'The growth parameter r must be between ' + str(self.map_rmin) + \
            ' and ' + str(self.map_rmax) + '.'
        return r * x * (1.0 - x)

class Logistic(Map):
    """Class for plotting a Logistic/Cubic/Sine Map """

    def __init__(self, r, n, x0, s=0, dotsonly=False, map='logistic'):
        Map.__init__(self, map=map)

        self.r = r    # Growth rate parameter

        assert n > 0, 'The number of iterations must be greater than zero.'
        self.n = n    # Number of iterations

        assert s >= 0, 'You cannot skip a negative number of iterations.'
        self.s = s    # Number of iterations to skip in the plot

        assert x0 >= 0 and x0 <= 1, \
            'The initial condition x0 should be in [0, 1].'
        self.x0 = x0  # The 1st initial condition

        self.x = self.y1 = []
        self.dotsonly = dotsonly

    def _plotline(self, x, y, color):
        """Plot the dots (x, y) connected by straight lines
           if the parameter 'dotsonly' if set to False """

        assert x.any() and y.any(), '_plotline(): internal error'

        plt.plot(x, y, color=color, linestyle='',
                 markerfacecolor=color, marker='o', markersize=8)
        if not self.dotsonly: plt.plot(x, y, color=color, alpha=0.6)

    def getxy(self):
        """Set the numpy vectors 'x' and 'y1' containing
           the iterations (1..n) and the corresponding values
           of the Logistic Equation rx(1-x) """

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
        """Plot a Logistic Equation map or the Final State Diagram """

        self.getxy()

        plt.suptitle('Dynamic Systems and Chaos', fontsize=14, fontweight='bold')
        plt.title('Logistic Equation')
        plt.xlabel('time t')
        plt.ylim([0, 1.])
        plt.grid(True)
        self._plotline(self.x[self.s:], self.y1[self.s:], 'mediumseagreen')

        plt.show()


class FinalState(Logistic):
    """Derived class for plotting a Final State Diagram """

    # By default, set the initial state to .5
    # make 3000 iterations and do no plot the first 2000 ones
    def __init__(self, r, n=1000, x0=.5, s=2000, map='logistic'):
        Logistic.__init__(self, r, n, x0, s, map)

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
        plt.title('Final State Diagram')

        plt.xlim([0, 1.])
        plt.ylim([0, 1.])
        plt.yticks([])

        plt.grid(True)

        plt.plot([0, 1], [.5, .5], color='black', lw=1)
        plt.plot(self.x[self.s:], self.y1[self.s:], color='black', linestyle='',
                 markerfacecolor='black', marker='o', markersize=8)

        plt.text(.05, .4, 'r = ' + str(self.r), style='italic',
                 bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})

        plt.show()


class LogisticDiff(Logistic):
    """Derived class for plotting a Logistic/Cubic/Sine Map
       with two different initial conditions, followed by a plot of
       their differences (for a visualization of the Butterfly Effect) """

    def __init__(self, r, n, x0, x1, s=0, dotsonly=False, map='logistic'):
        Logistic.__init__(self, r, n, x0, s, dotsonly, map)

        assert x1 >= 0 and x1 <= 1, \
            'The initial condition x1 should be in [0, 1].'
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
        """Plot a Logistic Equation map with two different seeds (two plots)
           followed by their difference """

        self.getxy()

        plt.figure(1)
        plt.suptitle('Dynamic Systems and Chaos',
                     fontsize=14, fontweight='bold')

        plt.subplot(211)
        plt.title('Time series for a logistic equation with two different initial conditions')
        plt.ylabel(r'$y_1(t),\ y_2(t)$', fontsize=14)
        plt.ylim([0, 1.])
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
    def __init__(self, r, n=100, s=200, map='logistic'):
        Map.__init__(self, map=map)

        assert len(r) == 2, 'The growth rate vector should contains two elements'
        self.rmin = r[0]    # Growth rate range
        self.rmax = r[1]

        assert n > 0, 'The number of iterations must be greater than zero.'
        self.n = n    # Number of iterations

        assert s >= 0, 'You cannot skip a negative number of iterations.'
        self.s = s    # Number of iterations to skip in the plot

        self.map = map  # The map (function) to be used

    def plot(self):
        plt.suptitle('Dynamic Systems and Chaos', fontsize=14, fontweight='bold')
        plt.title('Bifurcation Diagram for the ' + self.map_description)

        plt.xlim([self.rmin, self.rmax])
        plt.xticks([round(i, 1) for i in np.linspace(self.rmin, self.rmax, 5)])
        plt.xlabel('r')

        plt.ylim([0, 1.])
        plt.ylabel('final states')

        for r in np.linspace(self.rmin, self.rmax, 1000):
            x, y = FinalState(r, self.n, .5, self.s, self.map).getxy(r)
            plt.plot(y[self.s:], x[self.s:], color='black', linestyle='',
                     markerfacecolor='black', marker=',', markersize=1)

        plt.show()


def test():
    # Test the class 'Logistic'
    sys.stdout.write("Running the tests for the class 'Logistic'...\n")
    r, n, x0 = 3.2, 100, 0.4
    le1 = Logistic(r, n, x0, False)
    x, y1 = le1.getxy()

    assert len(x) == n+1, "x should be a vector of size " + str(n+1)
    assert x[0] == 0, "x[0] should be 0"
    assert x[n] == n, "the last element of x should be equal to " + str(n)
    assert x.sum() == n*(n+1)/2, "the sum of the elements of x is not correct"

    assert len(y1) == n+1, "y1 should be a vector of size " + str(n+1)
    assert y1[0] == x0, "the first element of y1 should be equal to x0"
    assert y1[n] == y1[n-2], "y1 is expected to be periodic with period 2"
    assert y1[n-1] == y1[n-3], "y1 is expected to be periodic with period 2"

    # Test the class 'LogisticDiff'
    sys.stdout.write("Running the tests for the class 'LogisticDiff'...\n")
    r, n, x0, x1 = 4.0, 50, 0.2, 0.2000001
    le2 = LogisticDiff(r, n, x0, x1, False)
    x, y1, y2 = le2.getxy()

    assert len(x) == n+1, "x should be a vector of size " + str(n+1)
    assert x[0] == 0, "x[0] should be 0"
    assert x[n] == n, "the last element of x should be equal to " + str(n)
    assert x.sum() == n*(n+1)/2, "the sum of the elements of x is not correct"

    assert len(y1) == n+1, "y1 should be a vector of size " + str(n+1)
    assert y1[0] == x0, "the first element of y1 should be equal to x0"

    ydiff = le2.getdiffy()
    assert len(ydiff) == n+1, \
        "the vector y2-y1 should have a size equal to " + str(n+1)
    np.any(ydiff > 1e3) or np.any(ydiff < -1e3), \
        "the diff vector should show the Butterfly Effect"

    sys.stdout.write("All tests successfully passed!\n")
