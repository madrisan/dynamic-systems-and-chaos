#!/usr/bin/python3

# Common functions for Dynamic Systems and Chaos
# Copyright (C) 2018 Davide Madrisan <davide.madrisan@gmail.com>
# SPDX-License-Identifier: Apache-2.0

__author__ = "Davide Madrisan"
__copyright__ = "Copyright (C) 2016-2018 Davide Madrisan"
__license__ = "Apache License 2.0 (Apache-2.0)"
__version__ = "3"
__email__ = "davide.madrisan@gmail.com"
__status__ = "stable"

import sys

def copyleft(descr):
    """Print the Copyright message and License """

    writeln(descr + ' v.' +  __version__ + ' (' + __status__ +  ')')
    writeln(__copyright__ + ' <' + __email__ + '>')
    writeln('License: ' + __license__ + '\n')

def die(exitcode, message):
    """Print and error message and exit with 'exitcode' """

    progname = sys.argv[0]
    sys.stderr.write('%s: error: %s\n' % (progname, message))
    sys.exit(exitcode)

def writeln(line):
    """Print the given line to stdout followed by a newline """

    sys.stdout.write(line + '\n')
