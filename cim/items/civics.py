##
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
import random


class CivicBuilding(object):
    healthiness = 10


class PoliceStation(CivicBuilding):
    @property
    def healthiness(self):
        return int(random.gauss(super(PoliceStation, self).healthiness, 10))


class FireStation(CivicBuilding):
    pass


class Hospital(CivicBuilding):
    @property
    def healthiness(self):
        return int(random.gauss(super(Hospital, self).healthiness, 1))
