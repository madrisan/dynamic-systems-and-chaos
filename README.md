# Dynamical Systems and Chaos

## Software

The code is written in Python and compatible with both Python 2 and 3 (tested on Fedora 24 Workstation).

    legraph.py
    finalstate.py

## Some theory

### Logistic maps

The following examples are based on a very simple model of a _population_ where there is some limit to growth:

<p align="center">
   <i>f</i>(<i>x</i>) = <i>rx</i>(1-<i>x</i>)
</p>

_r_ is a growth parameter, _x_ is measured as a fraction of the _annihilation_ parameter, and
_f_(_x_) gives the population next year given _x_, the population this year.

A _dynamical system_ is an iterated function, a system that evolves in time according to a well-defined, _unchanging_ rule.
The number we start with is called the _seed_ or _initial condition_.
The resulting sequence of numbers is called the _itinerary_ or _orbit_.
It is also sometimes called a _time series_ or a _trajectory_.

## Examples

#### Dynamical System with two fixed points

In mathematics, a _fixed point_ of a function is an element of the function's domain that is mapped to itself by the function.
That is to say, _c_ is a fixed point of the function _f_(_x_) if and only if _f_(_c_) = _c_

The following example shows a periodic orbit with two fixed points.

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
