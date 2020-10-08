### File simpson.py
### Implements the Simpson's baby, dog an poison problem while crossing the river.

from search import *

class SimpsonPuzzle(ProblemState):
    """
    Homer Simpson has to move his daughter Maggie, his dog Santa's Little Helper,
    and a jar of rat poison that looks like candy across a river. He can only take
    one item in his boat at a time. He can't leave Maggie alone with the rat poison
    (or she will eat it) and he can't leave Santa's Little Helper alone with Maggie
    (because the dog will pester the girl).
    Each operator returns a new instance of this class representing
    the successor state.
    """


    def  __init__(self, baby, poison, dog, person):
        self.baby = baby
        self.poison = poison
        self.dog = dog
        self.person = person


    def __str__(self):

        """
        Required method for use with the Search class.
        Returns a string representation of the state.
        """
        return "(" + str(self.baby) + "," + str(self.poison) + "," + str(self.dog) + "," + str(self.person) + ")"


    def illegal(self):
        """
        Required method for use with the Search class.
        Tests whether the state is illegal.
        """
        if self.dog == self.baby and self.person != self.baby: return 1
        if self.poison == self.baby and self.person != self.baby: return 1
        if self.baby > 1 or self.poison > 1 or self.dog > 1 or self.person > 1: return 1
        if self.baby < 0 or self.poison < 0 or self.dog < 0 or self.person < 0: return 1
        return 0


    def equals(self, state):
        """
        Required method for use with the Search class.
        Determines whether the state instance and the given
        state are equal.
        """
        return self.baby == state.baby and self.poison == state.poison and self.dog == state.dog and self.person == state.person


    def take_Baby(self):
        return SimpsonPuzzle(self.baby + 1, self.poison, self.dog, self.person + 1)


    def return_Baby(self):
        return SimpsonPuzzle(self.baby - 1, self.poison, self.dog, self.person - 1)


    def take_Poison(self):
        return SimpsonPuzzle(self.baby, self.poison + 1, self.dog, self.person + 1)

    def return_Poison(self):
        return SimpsonPuzzle(self.baby, self.poison - 1, self.dog, self.person - 1)


    def take_Dog(self):
        return SimpsonPuzzle(self.baby, self.poison, self.dog + 1, self.person + 1)

    def return_Dog(self):
        return SimpsonPuzzle(self.baby, self.poison, self.dog - 1, self.person - 1)

    def return_Alone(self):
        return SimpsonPuzzle(self.baby, self.poison, self.dog, self.person - 1)



    def operatorNames(self):
        """
        Required method for use with the Search class.
        Returns a list of the operator names in the
        same order as the applyOperators method.
        """


        return ["take_Baby", "take_Poison", "take_Dog", "return_Baby", "return_Poison", "return_dog", "return_Alone"]


    def applyOperators(self):
        """
        Required method for use with the Search class.
        Returns a list of possible successors to the current
            state, some of which may be illegal.
            """
        return [self.take_Baby(), self.take_Poison(), self.take_Dog(), self.return_Baby(), self.return_Poison(), self.return_Dog(), self.return_Alone()]

Search(SimpsonPuzzle(0, 0, 0, 0), SimpsonPuzzle(1, 1, 1, 1))
