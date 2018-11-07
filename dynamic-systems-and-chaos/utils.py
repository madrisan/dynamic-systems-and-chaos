#!/usr/bin/python3

# Common functions for Dynamic Systems and Chaos
# Copyright (C) 2018 Davide Madrisan <davide.madrisan@gmail.com>
# SPDX-License-Identifier: Apache-2.0

__author__ = "Davide Madrisan"
__copyright__ = "Copyright (C) 2016-2018 Davide Madrisan"
__license__ = "Apache License 2.0 (Apache-2.0)"
__version__ = "4"
__email__ = "davide.madrisan@gmail.com"
__status__ = "stable"

def copyleft(descr):
    """Print the Copyright message and License """

    return ("{0} v.{1} ({2})\n{3} <{4}>\nLicense: {5}"
        .format(
            descr, __version__, __status__,
            __copyright__, __email__,
            __license__))

def die(exitcode, message):
    """Print and error message and exit with 'exitcode' """

    progname = sys.argv[0]
    sys.stderr.write('%s: error: %s\n' % (progname, message))
    sys.exit(exitcode)
