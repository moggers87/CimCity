##
# Copyright (C) 2013, 2014 Jessica Tallon
# Copyright (C) 2014, 2015 Matt Molyneaux
#
# This file is part of CimCity.
#
# CimCity is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# CimCity is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CimCity.  If not, see <http://www.gnu.org/licenses/>.
##

from __future__ import absolute_import, division, print_function, unicode_literals
import argparse

import cim

parser = argparse.ArgumentParser(description="A city simulator")
parser.add_argument("--version", action="version", version="%(prog)s {}".format(cim.VERSION))
parser.add_argument("people", type=int)
parser.add_argument("houses", nargs="?", type=int, default=0)

args = parser.parse_args()
p_len = int(args.people)
h_len = int(args.houses)

cim.main(p_len, h_len)
