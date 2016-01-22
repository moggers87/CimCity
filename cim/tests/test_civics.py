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

from cim.items import civics


class HealthinessTestCase(TestCase):
    def test_base_class(self):
        retval = civics.CivicBuilding().healthiness
        self.assertEqual(retval, 10)

    def test_police(self):
        retval = civics.PoliceStation().healthiness
        # result is random
        self.assertTrue(isinstance(retval, int))

    def test_fire(self):
        retval = civics.FireStation().healthiness
        self.assertEqual(retval, 10)

    def test_hospital(self):
        retval = civics.Hospital().healthiness
        # result is random
        self.assertTrue(isinstance(retval, int))
