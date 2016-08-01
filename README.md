# Dynamical Systems and Chaos

## Some theory

### Logistic maps

We start by considering a very simple _model of a population_ where there is some limit to growth:

<p align="center">
   <i>f</i>(<i>x</i>) = <i>rx</i>(1-<i>x</i>)
</p>

_r_ is a _growth parameter_, _x_ is measured as a fraction of the _annihilation_ parameter
(the variable _x_ is thus always between 0 and 1),
and _f_(_x_) gives the population next year given _x_, the population this year.

By iterating this function we can create a _dynamical system_, that is, a system that evolves in time according to a well-defined, unchanging rule.
The number we start with is called the _seed_ or _initial condition_.
The resulting sequence of numbers is called the _itinerary_ or _orbit_.
It is also sometimes called a _time series_ or a _trajectory_.

## Software

This project is written in Python and compatible with both Python 2 and 3 (tested on Fedora 24 Workstation).

* __legraph.py__: iterate the logistic equation for different _r_ and _x0_ values and make _time series plots_
* __finalstate.py__: iterate the logistic equation for different _r_ and _x0_ values and make _final state diagrams_
* __lelib.py__: a simple library that implements a few Python classes for computing the time series and make the plots

#### Programs Usage

    $ ./legraph.py --help
    Plot of Logistic Equation Time Series v.2 (stable)
    Copyright (C) 2016 Davide Madrisan <davide.madrisan.gmail.com>
    
    Usage:
      ./legraph.py --x0 <float> [--x1 <float>] [-d] -r <float> -n <int> [-s <int>]
      ./legraph.py -h
      ./legraph.py --run-tests
    
    Where:
      -0 | --x0: 1st initial condition
      -1 | --x1: 2nd initial condition (optional)
      -d | --dots-only: do not connect the dots with lines
      -r | --rate: growth rate parameter
      -s | --skip: skip plotting the first 's' iterations
      -n | --steps: number of iterations

## Examples

#### Dynamical System with a Periodic Orbit

The following example shows a periodic orbit with two fixed points.

In mathematics, a _fixed point_ of a function is an element of the function's domain that is mapped to itself by the function.
That is to say, _c_ is a fixed point of the function _f_(_x_) if and only if _f_(_c_) = _c_

    # initial condition: 0.4 - growth rate: 3.2 - 50 iterations starting from 0 (x0)
    ./legraph.py --x0 0.4 -r 3.2 -n 50

![alt tag](https://github.com/madrisan/dynamic-systems-and-chaos/blob/master/plots/plot01_le-periodic-orbit.png)

#### The Batterfly Effect

    ./legraph.py --x0 0.2 --x1 0.2000001 -r 4.0 -n 50
 
![alt tag](https://github.com/madrisan/dynamic-systems-and-chaos/blob/master/plots/plot02_le-sdic.png)

    ./legraph.py --x0 0.2 -r 3.6 -n 500

![alt tag](https://github.com/madrisan/dynamic-systems-and-chaos/blob/master/plots/plot03_le-sdic-dots-and-lines.png)

    ./legraph.py --x0 0.2 -r 3.6 -n 5000 --dots-only

![alt tag](https://github.com/madrisan/dynamic-systems-and-chaos/blob/master/plots/plot04_le-sdic-dotsonly.png)

    ./finalstate.py -r 3.614 -s 200 -n 300

![alt tag](https://github.com/madrisan/dynamic-systems-and-chaos/blob/master/plots/plot05_le-final-state-diagram.png)
