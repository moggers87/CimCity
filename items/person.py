##
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

import math
import settings
import random

#from exceptions.generic import CityCimException

class Person(object):

    # features
    gender = None
    age = 0
    health = 100
    partner = None
    parents = []
    dead = False

    def __init__(self):
        self.gender = random.choice(["Male", "Female"])

    def on_tick(self, next_person=None):
        if self.dead:
            return None

        self.age += 1

        # are they dead?
        if self.health == 0:
            self.dead = True
            return None

        if self.age >= settings.avarage_age:
            self.dead = True
            return None

        if next_person:
            # oh okay.
            if not self.partner and random.randint(0, 100) >= 75 and self.age >= 12 and self.age <= 60:
                self.marry(next_person)
                return None
            elif self.partner and random.randint(0, 100) >= 95 and self.age >= 15 and self.age <= 50:
                if self.partner.gender == self.gender and random.randint(0, 10000) >= 9998:
                    print "=> Gay couple produced a child!"
                    return self.produce_offspring()
                else:
                    return self.produce_offspring()

                return None
        
    def marry(self, person):
        self.partner = person
        person.partner = self

    def produce_offspring(self):
        if self.partner is None:
            raise Exception("Must have a pertner to give birth")

        np = Person()
        np.parents = [self, self.partner]
        return np
