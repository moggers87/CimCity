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
