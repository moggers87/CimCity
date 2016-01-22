##
# Copyright (C) 2015 Matt Molyneaux
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
from unittest import TestCase

from cim.items import person


class PersonTestCase(TestCase):
    def test_init(self):
        psn = person.Person()
        self.assertIn(psn.sex, ["Male", "Female"])

        class FakeHouse(object):
            def add_occupants(self, *args):
                self.args = args

        home = FakeHouse()
        psn = person.Person(home)
        self.assertEqual(home.args, ([psn],))

    def test_marriage(self):
        p1 = person.Person()
        p2 = person.Person()

        p1.marry(p2)
        self.assertEqual(p1, p2.partner)
        self.assertEqual(p1.partner, p2)

    def test_gay(self):
        p1 = person.Person()
        p2 = person.Person()
        p2.sex = p1.sex

        p1.marry(p2)
        self.assertTrue(p1.gay)
        self.assertTrue(p2.gay)

    def test_miracle(self):
        p1 = person.Person()
        p2 = person.Person()
        p2.sex = p1.sex
        p1.marry(p2)
        child = p1.produce_offspring()

        self.assertTrue(child.miracle_child)

        child.parents = [p1]
        self.assertFalse(child.miracle_child)
