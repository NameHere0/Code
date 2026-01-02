"""
Docstring for Python.TikTakToe.index

Winning lines = [0, 1, 2], [3, 4, 5], [6, 7, 8]
                [0, 3, 6], [1, 4, 7], [2, 5, 8]
                [0, 4, 8], [2, 4, 6]
"""

winningLines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]


class Player:
    def __init__(self):
        self.takenSpaces = []

    def play(self):
        move = int(input("Where do you wanna move (0-8): "))

        self.takenSpaces.append(move)


player = Player()
player.play()
player.play()


def checkBestMove():
    for line in winningLines:
        missing = []

        countMissing: int = 0
        for space in line:
            if space in player.takenSpaces:
                countMissing += 1
            else:
                missing.append(space)

    if countMissing == 2 and len(missing) == 1:
        print(f"{missing[0]}")


print(checkBestMove())

#UNFINISHED
