<a href='https://ko-fi.com/K3K57TH3' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://az743702.vo.msecnd.net/cdn/kofi2.png?v=0' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>

# Dynamical Systems and Chaos

![Release Status](https://img.shields.io/badge/status-stable-brightgreen.svg)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9aeecdd2b382411b9f55d71edc6946ea)](https://www.codacy.com/app/madrisan/dynamic-systems-and-chaos?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=madrisan/dynamic-systems-and-chaos&amp;utm_campaign=Badge_Grade)
[![Code Climate](https://api.codeclimate.com/v1/badges/dbff89213a50df63fc01/maintainability)](https://codeclimate.com/github/madrisan/dynamic-systems-and-chaos/maintainability)
[![License](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](https://spdx.org/licenses/Apache-2.0.html)

[![Total alerts](https://img.shields.io/lgtm/alerts/g/madrisan/dynamic-systems-and-chaos.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/madrisan/dynamic-systems-and-chaos/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/madrisan/dynamic-systems-and-chaos.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/madrisan/dynamic-systems-and-chaos/context:python)

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

The software is written in Python and compatible with both Python 2 and 3 (tested on Fedora 24 through Fedora 30 Workstation), but if you want to run it under Python 2, you need to modify the shebang line of each Python script.

<dl>
  <dt>legraph.py -- Plot Logistic, Cube, and Sine orbits</dt>
  <dd>Iterate a logistic, cube, or sine equation for different <em>r</em> and <em>x0</em> values and make <em>time series plots</em>;</dd>

  <dt>finalstate.py -- Plot Final State Diagrams</dt>
  <dd>Iterate a logistic, cube, or sine equation for different <em>r</em> and <em>x0</em> values and plot the <em>final state diagram</em>;</dd>

  <dt>bifurcation.py -- Plot Bifurcations Diagrams</dt>
  <dd>Plot the <em>bifurcation diagram</em> of a cubic, logistic (default), or sine maps;</dd>

  <dt>lelib.py -- Object-oriented core library for computing and plotting</dt>
  <dd> A simple object-oriented Python library for <em>computing</em> time series and <em>plotting</em> orbits, final state and bifurcations diagrams.</dd>
</dl>

The core library requires the (widely-available and very popular) Python libraries `NumPy` and `matplotlib`.

### Working With Python3.3+ Virtual Environments

When testing `dynamic-systems-and-chaos` it's easier to use a virtual environment.
Python 3 presents a few steps to ensure you are actually installing and working with files inside of your virtual environment.
Refer to the original Python documentation
[Installing Packages Using pip and virtualenv](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/)
for the official instructions on this topic.

#### `dynamic-systems-and-chaos` virtual Environment Example

Create a virtual environment named `.venv` inside the git repository root:
```
$ python3 -m venv .venv
Using base prefix '/usr'
New python executable in /home/myself/dynamic-systems-and-chaos/.venv/bin/python3
Also creating executable in /home/myself/dynamic-systems-and-chaos/.venv/bin/python
Installing setuptools, pip, wheel...done.
```

Now that a virtualenv has been created in our `.venv` folder we should activate the virtual environment.
```
$ source .venv/bin/activate
(.venv)$
```
The virtual environment contains no extra modules needed to run `dynamic-systems-and-chaos`.
Therefore, we want to install the dependencies from the `requirements.txt` file.
However, we want to specify that we're using the virtual environment `pip3`:

```
(.venv)$ .venv/bin/pip3 install -r requirements.txt
Collecting cycler==0.10.0 (from -r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/f7/d2/e07d3ebb2bd7af696440ce7e754c59dd546ffe1bbe732c8ab68b9c834e61/cycler-0.10.0-py2.py3-none-any.whl
Collecting kiwisolver==1.1.0 (from -r requirements.txt (line 2))
  Using cached https://files.pythonhosted.org/packages/93/f8/518fb0bb89860eea6ff1b96483fbd9236d5ee991485d0f3eceff1770f654/kiwisolver-1.1.0-cp37-cp37m-manylinux1_x86_64.whl
Collecting matplotlib==3.1.1 (from -r requirements.txt (line 3))
  Using cached https://files.pythonhosted.org/packages/19/7a/60bd79c5d79559150f8bba866dd7d434f0a170312e4d15e8aefa5faba294/matplotlib-3.1.1-cp37-cp37m-manylinux1_x86_64.whl
Collecting numpy==1.17.2 (from -r requirements.txt (line 4))
  Using cached https://files.pythonhosted.org/packages/ba/e0/46e2f0540370f2661b044647fa447fef2ecbcc8f7cdb4329ca2feb03fb23/numpy-1.17.2-cp37-cp37m-manylinux1_x86_64.whl
Collecting pyparsing==2.4.2 (from -r requirements.txt (line 5))
  Using cached https://files.pythonhosted.org/packages/11/fa/0160cd525c62d7abd076a070ff02b2b94de589f1a9789774f17d7c54058e/pyparsing-2.4.2-py2.py3-none-any.whl
Collecting python-dateutil==2.8.0 (from -r requirements.txt (line 6))
  Using cached https://files.pythonhosted.org/packages/41/17/c62faccbfbd163c7f57f3844689e3a78bae1f403648a6afb1d0866d87fbb/python_dateutil-2.8.0-py2.py3-none-any.whl
Collecting six==1.12.0 (from -r requirements.txt (line 7))
  Using cached https://files.pythonhosted.org/packages/73/fb/00a976f728d0d1fecfe898238ce23f502a721c0ac0ecfedb80e0d88c64e9/six-1.12.0-py2.py3-none-any.whl
Requirement already satisfied: setuptools in ./.venv/lib/python3.7/site-packages (from kiwisolver==1.1.0->-r requirements.txt (line 2)) (41.4.0)
Installing collected packages: six, cycler, kiwisolver, numpy, python-dateutil, pyparsing, matplotlib
Successfully installed cycler-0.10.0 kiwisolver-1.1.0 matplotlib-3.1.1 numpy-1.17.2 pyparsing-2.4.2 python-dateutil-2.8.0 six-1.12.0
```

The output above is an example of already cached modules being installed.
These packages could also be outdated so please remember it's just an example.

You are now ready to start running and testing `dynamic-systems-and-chao` with a virtual environment using Python 3.

### Available Scripts

##### legraph.py

    $ ./legraph.py --help
    usage: legraph.py [-h] -0 X0 [-1 X1] [-d] -r R [-s S] -n N
                      [-m {logistic,cubic,sine}]
    
    Plot of Logistic Equation Time Series v.4 (stable)
    Copyright (C) 2016-2018 Davide Madrisan <davide.madrisan@gmail.com>
    License: Apache License 2.0 (Apache-2.0)
    
    optional arguments:
      -h, --help            show this help message and exit
      -0 X0, --x0 X0        1st initial condition
      -1 X1, --x1 X1        2nd initial condition (optional)
      -d, --dots-only       do not connect the dots with lines (default: False)
      -r R, --rate R        growth rate parameter
      -s S, --skip S        skip plotting the first 's' iterations
      -n N, --steps N       number of iterations
      -m {logistic,cubic,sine}, --map {logistic,cubic,sine}
                            select the desired map (logistic, cubic, or sine)
    
    Examples:
    
    # time series with a stable fixed point
    legraph.py -0 0.4 -r 3.2 -n 50
    legraph.py -0 0.4 -1 0.45 -r 3.2 -n 50
    # chaotic results (randon output)
    legraph.py --x0 0.2 --x1 0.2000001 -r 4.0 -n 50
    legraph.py -0 0.2 -r 3.6 -n 5000 --dots-only
    legraph.py -0 0.9 -r 4.5 -n 50 --map=cubic
    legraph.py -0 0.4 -r 0.8 -n 50 --map=sine

##### finalstate.py

    $ ./finalstate.py --help
    usage: finalstate.py [-h] [-0 X0] -r R [-s S] [-n N]
                         [-m {logistic,cubic,sine}]
    
    Plot of the Final State Diagram v.4 (stable)
    Copyright (C) 2016-2018 Davide Madrisan <davide.madrisan@gmail.com>
    License: Apache License 2.0 (Apache-2.0)
    
    optional arguments:
      -h, --help            show this help message and exit
      -0 X0, --x0 X0        initial condition (default: 0.5)
      -r R, --rate R        growth rate parameter
      -s S, --skip S        skip plotting the first 's' iterations (default: 2000)
      -n N, --steps N       number of iterations (default: 1000)
      -m {logistic,cubic,sine}, --map {logistic,cubic,sine}
                            select the desired map (logistic, cubic, or sine)
    
    Examples:
    
    finalstate.py -r 3.492
    finalstate.py -r 3.614 -s 200 -n 300
    finalstate.py -0 0.4 -r 3.2 -s 10 -n 50
    finalstate.py -0 0.8 -r 6.2 -n 20 --map=cubic

##### bifurcations.py

    $ ./bifurcations.py --help
    Plot the Bifurcation Diagram of Logistic, Cubic, and Sine Maps v.4 (stable)
    Copyright (C) 2016-2018 Davide Madrisan <davide.madrisan@gmail.com>
    License: Apache License 2.0 (Apache-2.0)
    
    usage: bifurcations.py [-h] [-r R] [-y Y] [-s S] [-n N]
                           [-m {logistic,cubic,sine}]
    
    optional arguments:
      -h, --help            show this help message and exit
      -r R, --rate R        range of the growth rate parameter (default: the
                            entire range)
      -y Y, --people Y      normalized range of the population (default: the
                            entire range)
      -s S, --skip S        skip plotting the first 's' iterations (default: 200)
      -n N, --steps N       number of iterations (default: 100)
      -m {logistic,cubic,sine}, --map {logistic,cubic,sine}
                            select the desired map (logistic, cubic, or sine)
    
    Examples:
    
    bifurcations.py -r 1:4
    bifurcations.py -r 4:6.5 --map=cubic
    bifurcations.py --map=sine -s 200 -n 200
    bifurcations.py -r 3.:4. -s 500 -n 600
    bifurcations.py -r 3.5:3.6 -y .3:.6 -s 800 -n 1000

## Examples

#### Dynamical System with a Periodic Orbit

The following example shows a periodic orbit with two fixed points.

In mathematics, a _fixed point_ of a function is an element of the function's domain that is mapped to itself by the function.
That is to say, _c_ is a fixed point of the function _f_(_x_) if and only if _f_(_c_) = _c_

    # initial condition: 0.4 - growth rate: 3.2 - 50 iterations starting from 0 (x0)
    ./legraph.py --x0 0.4 -r 3.2 -n 50

![alt tag](https://github.com/madrisan/dynamic-systems-and-chaos/blob/master/plots/plot01_le-periodic-orbit.png)

#### Aperiodic Orbits and The Batterfly Effect

For _r_ = 4 (and other values), the orbit is aperiodic: it never repeats.
Applying the same function over and over again does not result in periodic behavior.

We can use `legraph.py` to compare time series for two different initial conditions.

    ./legraph.py --x0 0.2 --x1 0.2000001 -r 4.0 -n 50

The bottom plot is the difference between the two time series in the top plot.

You can note that the two orbits start very close together and eventually end up far apart.
This is known as _sensitive dependence on initial conditions_ (_SDIC_), or the _butterfly effect_.

The latter name cames from the title of a 1979 paper by Ed Lorenz called
"Predictability: Does the Flap of a Butterfly's Wings in Brazil Set Off a Tornado in Texas?".
The idea is that in a chaotic system, small disturbances grow exponenfially fast, rendering long-term prediction
impossible.

More precisely, for any initial condition _x_ there is another initial condition very near to it that eventually
ends up far away.
To predict the behavior of a system with _SDIC_ requires knowing the initial condition with _impossible accuracy_.
Systems with _SDIC_ are deterministic yet unpredictable in the long run.

![alt tag](https://github.com/madrisan/dynamic-systems-and-chaos/blob/master/plots/plot02_le-sdic.png)

#### Aperiodic Orbits with holes

The aperiodic orbits are always bounded but do not necessarily cover all the domain. They can present one or more holes.

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

We can "glue" together the final state diagrams made for different values of the parameter _r_
to make a _bifurcation diagram_, that lets us see, all at once, all the different behaviour exhibited by a
dynamical system as we vary the parameter _r_.

##### Logistic Map

The script `bifurcations.py` lets us plot the _bifurcation diagram_ of the logistic map (the map selected by default)

<p align="center">
   <i>f</i>(<i>x</i>) = <i>rx</i>(1-<i>x</i>)
</p>

    ./bifurcations.py -r 2:4 -n 300 -s 400

![alt tag](https://github.com/madrisan/dynamic-systems-and-chaos/blob/master/plots/plot07_le-bifurcation-diagram-le.png)

##### Cubic Map

We can plot the _bifurcation diagram_ of the _cubic map_

<p align="center">
   <i>f</i>(<i>x</i>) = <i>rx</i><sup>2</sup>(1-<i>x</i>)
</p>

by adding the command-line switch `--map=cubic`

    ./bifurcations.py -r 4:6.5 --map=cubic

![alt tag](https://github.com/madrisan/dynamic-systems-and-chaos/blob/master/plots/plot08_le-bifurcation-diagram-cubic.png)

##### Sine Map

And finally plot the _bifurcation diagram_ of the _sine map_

<p align="center">
   <i>f</i>(<i>x</i>) = <i>r sin</i>(<sup>&pi;<i>x</i></sup>&frasl;<sub>2</sub>)
</p>

by using the command-line switch `--map=sine`

    ./bifurcations.py --map=sine -s 200 -n 200

![alt tag](https://github.com/madrisan/dynamic-systems-and-chaos/blob/master/plots/plot09_le-bifurcation-diagram-sine.png)

You can note the similarities between the three bifurcation diagrams (and all the ones generated by the class of
iterated functions that map an interval to itself and have a single quadratic maximum.)

This is a well known result that came from the amazing phenomenon of the _universality of the period-doubling route to chaos_
(also known as [_Feigenbaum's constant_](https://en.wikipedia.org/wiki/Feigenbaum_constants)).
The physicist Mitchell Feigenbaum in fact showed that there are certain universal laws governing the transition from
regular to chaotic behaviour, His predictions were confirmed in experiments on electronic circuits, swirling fluids,
chemical reactions, semiconductors, and heard cells. Feigenbaum's laws transcended the superficial differences between heart
cells and and silicon semiconductors. Different materials, the same laws of chaos!

## References and Acknowledgments

This software has been developed as part of the (optional) homeworks of the
[MOOC](https://www.complexityexplorer.org/courses/61-introduction-to-dynamical-systems-and-chaos-summer-2016)
__Introduction to Dynamical Systems and Chaos__ (Summer, 2016), leaded by __David Feldman__, Professor of Physics and Mathematics at College of the Atlantic.

For more details about the chaos and sync theories, see the Steven Strogatz's books "Sync" and "Nonlinear Dynamics and Chaos".
Or the David Feldman's introductory book "Chaos and Fractals: An Elementary Introduction".
