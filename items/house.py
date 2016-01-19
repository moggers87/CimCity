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

import settings


__all__ = ['homeless', 'House']


class LivingSpace(object):
    """Maybe house"""
    healthiness = 0

    def __init__(self):
        self.occupants = set()

    def __len__(self):
        return len(self.occupants)

    def add_occupants(self, people):
        """Move person to this house, returns people it can't fit in"""
        while True:
            if self.full():
                return people

            try:
                person = people.pop(0)
            except IndexError:
                return people

            if hasattr(person, "home"):
                person.home.occupants.remove(person)

            person.home = self
            person.healthiness = self.healthiness
            self.occupants.add(person)

    def full(self):
        return len(self) == self.capacity

    def recalculate_health(self, person=None):
        if person:
            person.healthiness = self.healthiness

        for occupant in self.occupants:
            occupant.healthiness = self.healthiness


class Homeless(LivingSpace):
    """Not a house"""
    capacity = None
    healthiness = settings.homeless_healthiness

homeless = Homeless()


class House(LivingSpace):
    """Basic house"""
    capacity = 4
    base_healthiness = 0

    def __init__(self, civics=None):
        self.civics = set(civics or [])
        super(House, self).__init__()

    def recalculate_health(self, person=None):
        healthiness = self.base_healthiness
        for civic in self.civics:
            healthiness = healthiness + civic.healthiness
        self.healthiness = healthiness

        super(House, self).recalculate_health(person)
