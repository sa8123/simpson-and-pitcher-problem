from informedSearch import *

class EightPuzzle(InformedProblemState):

    def __init__(self, puzzle):
        self.puzzle = puzzle;

    def __str__(self):
        firstRow = self.puzzle[:3]
        secondRow = self.puzzle[3:6]
        thirdRow = self.puzzle[6:9]
        toPrint = firstRow + "\n" + secondRow +  "\n" + thirdRow + "\n"
        return toPrint

    def illegal(self):
        if self.puzzle == -1: return 1
        return 0

    def equals(self, state):
        return self.puzzle == state.puzzle


    def move_Left(self):
        temp = self.puzzle.index('0')
        if temp not in (0, 3, 6):
            index = temp - 1
            newboard = ""
            newboard = self.puzzle[0:index] + '0' + self.puzzle[index] + self.puzzle[temp + 1:]
            return EightPuzzle(newboard)
        return EightPuzzle(-1)

    def move_Right(self):
        temp = self.puzzle.index('0')
        if temp not in (2, 5, 8):
            temp1 = temp + 1
            newBoard = ""
            newBoard = self.puzzle[0:temp] + self.puzzle[temp1] + '0' + self.puzzle[temp1 + 1:]
            return EightPuzzle(newBoard)
        return EightPuzzle(-1)

    def move_Down(self):
        temp = self.puzzle.index('0')
        if temp not in (6, 7, 8):
            temp1 = temp + 3
            newBoard = ""
            newBoard = self.puzzle[0:temp] + self.puzzle[temp1] + self.puzzle[temp + 1: temp1] + '0' + self.puzzle[temp1 + 1:]
            return EightPuzzle(newBoard)
        return EightPuzzle(-1)

    def move_Up(self):
        temp = self.puzzle.index('0')
        if temp not in (0, 1, 2):
            temp1 = temp - 3
            newBoard = ""
            newBoard = self.puzzle[0:temp1] + '0' + self.puzzle[temp1+1: temp] + self.puzzle[temp1] + self.puzzle[temp + 1:]
            return EightPuzzle(newBoard)
        return EightPuzzle(-1)

    def operatorNames(self):
        return ["move_Left", "move_Right", "move_Up", "move_Down"]

    def applyOperators(self):
        return [self.move_Left(), self.move_Right(), self.move_Up(), self.move_Down()]

    def heuristic(self, goal):
        # sum = 0
        temp = 0
        # sum = PuzzleState.outOfPlace(self, goal
        sum1 = EightPuzzle.manhattan(self, goal)
        #temp = temp + sum1
        #sum2 = EightPuzzle.out_Place(self,goal)
        #sum = sum1 + sum2

        return sum1

    def manhattan(self, goal):
        sum1 = 0
        for i in range(3):
            for j in range(3):
                sum1 += int(abs(self.puzzle.index(i) - goal.puzzle.index(j)))
        return sum1

    def out_Place(self, goal):
        sum = 0
        for i in range(0, 9):
            if self.puzzle[i] != goal.puzzle[i]:
                sum += 1
        return sum

goal = '123804765'
a = '130824765'
b = '134862075'
c = '013425876'
d = '712803654'
e = '812704653'
f = '263405187'
g = '734615802'
h = '745603812'
InformedSearch(EightPuzzle(h), EightPuzzle(goal))
"""
InformedSearch(EightPuzzle(b), EightPuzzle(goal))
InformedSearch(EightPuzzle(c), EightPuzzle(goal))
InformedSearch(EightPuzzle(d), EightPuzzle(goal))
InformedSearch(EightPuzzle(e), EightPuzzle(goal))
InformedSearch(EightPuzzle(f), EightPuzzle(goal))
InformedSearch(EightPuzzle(g), EightPuzzle(goal))
InformedSearch(EightPuzzle(h), EightPuzzle(goal))
"""










