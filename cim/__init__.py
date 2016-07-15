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
from threading import Timer
import argparse
import sys

from cim.items.house import *
from cim.items.person import Person
from cim import settings


VERSION = "0.0.1"

# globals
ticks = 0

def alive(people):
    return len([p for p in people if not p.dead])


def dead(people):
    return len([p for p in people if p.dead])


def display(people, ticks):
    msg = "Alive: %s | Dead: %s | Homeless: %s | ticks %s\r"
    msg = msg % (alive(people), dead(people), len(homeless), ticks)
    sys.stdout.write(msg)
    sys.stdout.flush()


class GayOnExit(object):
    """Gay context manager

    Counts out how many couples with same-sex and finds all the miracle
    children.
    """

    def __init__(self, people):
        """Takes list of people"""
        self.people = people

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is KeyboardInterrupt or exc_type is None:
            print("\r", end="")
            display(self.people, ticks)
            print()

            miracle_childs = 0
            gay_couples = 0
            for i in self.people:
                if i.gay:
                    gay_couples += 1
                if i.miracle_child:
                    miracle_childs += 1

            # assume monogamy
            gay_couples = gay_couples / 2
            popn = len(self.people)

            ratio = 100 * gay_couples / popn
            print("Percentage of same-sex couples: %f" % ratio)

            print("Number of miracle children: %d" % miracle_childs)

            return True
        return False


def main(p_len, h_len):
    global ticks
    # inital people gen
    people = [Person() for i in range(p_len)]
    houses = [House() for i in range(h_len)]

    print("Initial people: %d | Initial houses: %d" % (p_len, h_len))

    left_over = people[:]
    for house in houses:
        if not house.add_occupants(left_over):
            break

    homeless.add_occupants(left_over)

    c = 0
    ticks = 0
    speed = 60 / settings.speed

    with GayOnExit(people):
        while alive(people) > 0:
            timer = Timer(speed, lambda *x: x)
            timer.start()

            display(people, ticks)

            # iterate over people, including those born this generation
            while True:
                try:
                    person = people[c]
                except IndexError:
                    break

                c += 1

                try:
                    np = person.on_tick(people[c])
                except IndexError:
                    np = person.on_tick()

                if np:
                    people.append(np)
                    np = [np]
                    for house in houses:
                        if not house.add_occupants(np):
                            break
                    homeless.add_occupants(np)

            ticks += 1
            c = 0
            timer.join()


def run():
    # script entry point
    parser = argparse.ArgumentParser(description="A city simulator")
    parser.add_argument("--version", action="version", version="%(prog)s {}".format(VERSION))
    parser.add_argument("people", type=int)
    parser.add_argument("houses", nargs="?", type=int, default=0)

    args = parser.parse_args()
    p_len = int(args.people)
    h_len = int(args.houses)

    main(p_len, h_len)
