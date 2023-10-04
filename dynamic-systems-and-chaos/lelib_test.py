#!/usr/bin/python3

# Logistic Equation Library - Unit tests
# Copyright (C) 2016-2019 Davide Madrisan <davide.madrisan@gmail.com>
# SPDX-License-Identifier: Apache-2.0

from __future__ import print_function
import numpy as np

from lelib import Map, Logistic, LogisticDiff


def test_class_map():
    """Test the class 'Map'"""

    print("Running the tests for the class 'Map'...")

    m = Map()
    m.ensure(m.map_name == "logistic", "The default map should be 'logistic'")
    m.ensure(m.map_longname == "Logistic Equation", "Logistic Map: bad long name")
    m.ensure(m.map_rmin == 0 and m.map_rmax == 4, "Logistic Map: bad range for r")
    m.ensure(m.map_ymin == 0 and m.map_ymax == 1, "Logistic Map: bad range for y")
    i = m.map(4, 0.25)
    m.ensure(i == 0.75, "Logistic Map: bad value for r=4 and x=.25: should be %f" % i)

    m = Map("cubic")
    m.ensure(m.map_name == "cubic", "Cubic Map: bad map selection")
    m.ensure(m.map_longname == "Cubic Equation", "Cubic Map: bad long name")
    m.ensure(m.map_rmin == 0 and m.map_rmax == 6.5, "Cubic Map: bad range for r")
    m.ensure(m.map_ymin == 0 and m.map_ymax == 1, "Cubic Map: bad range for y")
    i = m.map(2, 0.5)
    m.ensure(i == 0.25, "Cubic Map: bad value for r=2 and x=.5, should be %f" % i)

    m = Map("sine")
    m.ensure(m.map_name == "sine", "Sine Map: bad map selection")
    m.ensure(m.map_longname == "Sine Equation", "Sine Map: bad long name")
    m.ensure(m.map_rmin == 0 and m.map_rmax == 2, "Sine Map: bad range for r")
    m.ensure(m.map_ymin == 0 and m.map_ymax == 2, "Sine Map: bad range for y")
    i = m.map(0.5, 1)
    m.ensure(i == 0.5, "Sine Map: bad value for r=0.5 and x=1: should be %f" % i)


def test_class_logistic():
    """Test the class 'Logistic'"""

    print("Running the tests for the class 'Logistic'...")

    r, n, x0 = 3.2, 100, 0.4
    le1 = Logistic(r, n, x0, False, "logistic")
    x, y1 = le1.getxy()

    m = Map()
    m.ensure(len(x) == n + 1, "x should be a vector of size %d" % (n + 1))
    m.ensure(x[0] == 0, "x[0] should be 0")
    m.ensure(x[n] == n, "the last element of x should be equal to %d" % n)
    m.ensure(x.sum() == n * (n + 1) / 2, "the sum of the elements of x is not correct")

    m.ensure(len(y1) == n + 1, "y1 should be a vector of size %d" % (n + 1))
    m.ensure(y1[0] == x0, "the first element of y1 should be equal to x0")
    m.ensure(y1[n] == y1[n - 2], "y1 is expected to be periodic with period 2")
    m.ensure(y1[n - 1] == y1[n - 3], "y1 is expected to be periodic with period 2")


def test_class_logisticdiff():
    """Test the class 'LogisticDiff'"""

    print("Running the tests for the class 'LogisticDiff'...")

    r, n, x0, x1 = 4.0, 50, 0.2, 0.2000001
    le2 = LogisticDiff(r, n, x0, x1, False, "logistic")
    x, y1, _ = le2.getxy()

    m = Map()
    m.ensure(len(x) == n + 1, "x should be a vector of size %d" % (n + 1))
    m.ensure(x[0] == 0, "x[0] should be 0")
    m.ensure(x[n] == n, "the last element of x should be equal to %d" % n)
    m.ensure(x.sum() == n * (n + 1) / 2, "the sum of the elements of x is not correct")

    m.ensure(len(y1) == n + 1, "y1 should be a vector of size %d" % (n + 1))
    m.ensure(y1[0] == x0, "the first element of y1 should be equal to x0")

    ydiff = le2.getdiffy()
    m.ensure(
        len(ydiff) == n + 1, "the vector y2-y1 should have a size equal to %d" % (n + 1)
    )
    m.ensure(
        np.all(ydiff < 1e3) and np.all(ydiff > -1e3),
        "the diff vector should show the Butterfly Effect",
    )


def tests():
    test_class_map()
    test_class_logistic()
    test_class_logisticdiff()
