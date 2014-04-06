import settings

__all__ = ['homeless', 'House']

class LivingSpace(object):
    """Maybe house"""
    healthiness = 0

    def __init__(self, occupants=None):
        self.occupants = set()
        self.add_occupants(occupants or [])

        self.recalculate_health()

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
            self.occupants.add(person)

    def full(self):
        return len(self) == self.capacity

    def recalculate_health(self):
        for occupant in self.occupants:
            occupant.healthiness = healthiness

class Homeless(LivingSpace):
    """Not a house"""
    capacity = None
    healthiness = min(0, settings.homeless_healthiness)
    
homeless = Homeless()

class House(LivingSpace):
    """Basic house"""
    capacity = 4

    def __init__(self, occupants=None, civics=None):
        self.civics = set(civics or [])
        super(House, self).__init__(occupants)

    def recalculate_health(self):
        healthiness = 0
        for civic in self.civics:
            healthiness = healthiness + civic.healthiness
        self.healthiness = healthiness

        super(House, self).recalculate_health()
