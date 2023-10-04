#!/usr/bin/env python

from setuptools import setup

DESCRIPTION = """Dynamic Systems and Chaos Plot Generator.

This software has been developed as part of the (optional) homeworks of the
MOOC "Introduction to Dynamical Systems and Chaos (Summer, 2016)", leaded by
David Feldman, Professor of Physics and Mathematics at College of the Atlantic.

It let you plot the orbit of a Logistic, Cubic, or Sine Map, the two orbits of a
Logistic, Cubic, or Sine Map with two different starting points (along with the
plot of the differences between the two maps), and the Final State and
Bifurcation Diagrams.
"""

DOCLINES = DESCRIPTION.split("\n")

CLASSIFIERS = """\
Development Status :: 5 - Production/Stable
Intended Audience :: Education
Intended Audience :: Science/Research
License :: OSI Approved :: Apache Software License
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 3
Topic :: Scientific/Engineering :: Mathematics
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
"""

VERSION = "2"

setup(
    name="dynamic-systems-and-chaos",
    description=DOCLINES[0],
    long_description=DESCRIPTION,
    version=VERSION,
    url="https://github.com/madrisan/dynamic-systems-and-chaos/",
    author="Davide Madrisan",
    author_email="davide.madrisan@gmail.com",
    license="Apache License 2.0",
    packages=["dynamic-systems-and-chaos"],
    scripts=[
        "dynamic-systems-and-chaos/bifurcations.py",
        "dynamic-systems-and-chaos/finalstate.py",
        "dynamic-systems-and-chaos/legraph.py",
    ],
    classifiers=[_f for _f in CLASSIFIERS.split("\n") if _f],
    install_requires=[
        "numpy",
        "matplotlib",
    ],
    platforms=["Linux", "Mac OS-X", "Windows"],
)
