##
# Copyright (C) 2013, 2014 Jessica Tallon
# Copyright (C) 2014 Matt Molyneaux
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

import settings


class Person(object):

    # features
    sex = None
    age = 0
    health = 100
    healthiness = 0
    partner = None
    parents = []
    dead = False

    def __init__(self, home=None):
        self.sex = random.choice(["Male", "Female"])
        if home is not None:
            home.add_occupants([self])

    def on_tick(self, next_person=None):
        if self.dead:
            return None

        self.age += 1

        self.health = min(100, max(0, self.health + random.gauss(self.healthiness, 10)))

        # are they dead?
        if self.health == 0:
            return self.death()

        if (settings.avarage_age - random.gauss(self.age, 10)) <= 0:
            return self.death()

        if next_person:
            if not self.partner and random.randint(0, 100) >= 75 and self.age >= 12 and self.age <= 60:
                self.marry(next_person)
                return None
            elif self.partner and random.randint(0, 100) >= 80 and self.age >= 15 and self.age <= 50:
                if self.partner.sex == self.sex:
                    # same sex couple, massively reduced chance of producing a child!
                    if random.randint(0, 10000) >= 9998:
                        child = self.produce_offspring()

                        if child is not None:
                            print("\n=> Gay couple produced a child!")

                        return child
                else:
                    return self.produce_offspring()

    def marry(self, person):
        self.partner = person
        person.partner = self

    def produce_offspring(self):
        if self.partner is None:
            raise Exception("Must have a pertner to give birth")

        if self.health < 50:
            return None

        np = Person()
        np.parents = [self, self.partner]
        return np

    def death(self):
        self.dead = True
        self.home.occupants.remove(self)
        self.home = None

    @property
    def gay(self):
        """Is this person in a same-sex relationship?"""
        return self.partner is not None and self.sex == self.partner.sex

    @property
    def miricle_child(self):
        """Is this person the product of a same-sex couple?"""
        parents = [p.sex == self.parents[0].sex for p in self.parents]
        return len(self.parents) > 1 and all(parents)
