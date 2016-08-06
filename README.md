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
The resulting sequence of numbers

<p align="center">
   <i>x</i><small><sub>0</sub></small></br>
   <i>x</i><small><sub>1</sub></small> = <i>f</i>(<i>x</i><small><sub>0</sub></small>)</br>
   ...</br>
   <i>x</i><small><sub>n</sub></small> = <i>f</i>(<i>x</i><small><sub>n-1</sub></small>)</br>
</p>

is called the _itinerary_ or _orbit_ (or sometimes a _time series_ or a _trajectory_).

## Software

The software is written in Python and compatible with both Python 2 and 3 (tested on Fedora 24 Workstation).

* __legraph.py__: iterate the logistic equation for different _r_ and _x0_ values and make _time series plots_;
* __finalstate.py__: iterate the logistic equation for different _r_ and _x0_ values and make _final state diagrams_;
* __lelib.py__: a simple library that implements a few Python classes for computing the time series and make the plots;
* __bifurcation.sh: plot the _bifurcation diagram_ of a logistic equation.

#### How to use these scripts

##### legraph.py

    $ ./legraph.py --help
    Plot of Logistic Equation Time Series
    Copyright (C) 2016 Davide Madrisan <davide.madrisan@gmail.com>
    
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

##### finalstate.py

    $ ./finalstate.py --help
    Plot of the Final State Diagram
    Copyright (C) 2016 Davide Madrisan <davide.madrisan@gmail.com>
    
    Usage:
      ./finalstate.py [--x0 <float>] -r <float> [-n <int>] [-s <int>]
      ./finalstate.py -h
    
    Where:
      -0 | --x0: initial condition (default: .5)
      -r | --rate: growth rate parameter
      -s | --skip: skip plotting the first 's' iterations (default: 2000)
      -n | --steps: number of iterations (default: 3000)

##### bifurcations.py

    $ ./bifurcations.py --help
    Plot the Bifurcation Diagram of Logistic and Cubic Maps
    Copyright (C) 2016 Davide Madrisan <davide.madrisan@gmail.com>

    Usage:
      ./bifurcations.py [-r <float>:<float>] [-n <int>] [-s <int>] [--cubic]
      ./bifurcations.py -h

    Where:
      -r | --rate: range of the growth rate parameters (default: [0:4])
      -s | --skip: skip plotting the first 's' iterations (default: 200)
      -n | --steps: number of iterations (default: 100)
      -c | --cubic: plot the bifurcation diagram of the cubic map
      -l | --logistic: plot the diagram of the logistic map (default)

    Example:
      ./bifurcations.py -r 1:4
      ./bifurcations.py -r 4:6.5 --cubic
      ./bifurcations.py -r 2.:4. -s 500 -n 600

## Examples

#### Dynamical System with a Periodic Orbit

The following example shows a periodic orbit with two fixed points.

In mathematics, a _fixed point_ of a function is an element of the function's domain that is mapped to itself by the function.
That is to say, _c_ is a fixed point of the function _f_(_x_) if and only if _f_(_c_) = _c_

    # initial condition: 0.4 - growth rate: 3.2 - 50 iterations starting from 0 (x0)
    ./legraph.py --x0 0.4 -r 3.2 -n 50

![alt tag](https://github.com/madrisan/dynamic-systems-and-chaos/blob/master/plots/plot01_le-periodic-orbit.png)

#### Aperiodic Orbits and The Batterfly Effect

For _r_ = 4 (and other values), the orbit is aperiodic It never repeats.
Applying the same function over and over again does not result in periodic behavior.

We can use `legraph.py` to compare time series for two different initial conditions.

    ./legraph.py --x0 0.2 --x1 0.2000001 -r 4.0 -n 50

The bottom plot is the difference between the two time series in the top plot.

You can note that the two orbits start very close together and eventually end up far apart.
This is known as _sensitive dependence on initial conditions_ (_SDIC_), or the _butterfly effect_.

For any initial condition _x_ there is another initial condition very near to it that eventually ends up far away.
To predict the behavior of a system with _SDIC_ requires knowing the initial condition with _impossible accuracy_.
Systems with _SDIC_ are deterministic yet unpredictable in the long run.

![alt tag](https://github.com/madrisan/dynamic-systems-and-chaos/blob/master/plots/plot02_le-sdic.png)

#### Aperiodic Orbits with holes

The aperiodic orbits are always bounded nut do not necessarily cover all the domain. They can present one or more holes.

    ./legraph.py --x0 0.2 -r 3.6 -n 500

![alt tag](https://github.com/madrisan/dynamic-systems-and-chaos/blob/master/plots/plot03_le-sdic-dots-and-lines.png)

We can increase the number of iterations and add the command line switch `--dots-only` in order to better visualize this
behaviour.

    ./legraph.py --x0 0.2 -r 3.6 -n 5000 --dots-only

![alt tag](https://github.com/madrisan/dynamic-systems-and-chaos/blob/master/plots/plot04_le-sdic-dotsonly.png)

#### Final State Diagrams

For a given _r_ value, the program `finalstate.py` will iterate 1000 times by default (`-s`),
then plot the next 2000 iterates (`-n`) on the unit interval.
The resulting plot is called a _final-state diagram_.

The number of skipped (`-s`) and plotted (`-n`) iterations can be manually tuned as shown in the following example.

    ./finalstate.py -r 3.614 -s 200 -n 300

![alt tag](https://github.com/madrisan/dynamic-systems-and-chaos/blob/master/plots/plot05_le-final-state-diagram.png)

Here you can find an example of a final-state diagram generated by a periodic orbit.

    ./finalstate.py -r 3.2 -s 10 -n 50

![alt tag](https://github.com/madrisan/dynamic-systems-and-chaos/blob/master/plots/plot06_le-final-state-diagram.png)

#### Bifurcation Diagrams

##### Logistic Map

    ./bifurcations.py -r 2:4 -n 300 -s 400

![alt tag](https://github.com/madrisan/dynamic-systems-and-chaos/blob/master/plots/plot07_le-bifurcation-diagram-le.png)

##### Cubic Map

    ./bifurcations.py -r 4:6.5 --cubic

![alt tag](https://github.com/madrisan/dynamic-systems-and-chaos/blob/master/plots/plot08_le-bifurcation-diagram-cubic.png)

## References and Acknowledgments

This software has been developed as part of the (optional) homeworks of the
[MOOC](https://www.complexityexplorer.org/courses/61-introduction-to-dynamical-systems-and-chaos-summer-2016)
__Introduction to Dynamical Systems and Chaos__ (Summer, 2016), leaded by __David Feldman__, Professor of Physics and Mathematics at College of the Atlantic.
