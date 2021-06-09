# Simulating the roll of one die

from random import randint

class Die():
    """A class representing a single die."""

    # When die is created, the default numbers of sides is 6, unless otherwise specified.
    def __init__(self, num_sides = 6):
        """Assume a six-sided die."""
        self.num_sides = num_sides

    # Method to return which number the die landed up on. Randomly chosen between 1 and the number of sides.
    def roll(self):
        """Return a random value between 1 and the number of sides."""
        return randint(1, self.num_sides)

    