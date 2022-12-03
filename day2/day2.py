import sys
import os

def score(fileName):
    scores = {'X': 1, 'Y': 2, 'Z': 3}
    with open(fileName, "r") as f:
        totalScore = 0
        for line in f:
            # Truncate the newline character
            line = line[:-1] if line[-1] == '\n' else line
            line = chooseShape(line)
            totalScore += outcome(line) + scores[line[2]]
        print("total score: ", totalScore)

def outcome(shapes):
    
    if shapes in ["A X", "B Y", "C Z"]:
        return 3 # Draw
    elif shapes in ["A Z", "C Y", "B X"]:
        return 0 # Opponent/Player 1 wins
    elif shapes in ["C X", "B Z", "A Y"]:
        return 6 # Player wins
    else:
        return -1 # error, could also throw an exception if I wanted this to be more sophisticated

def chooseShape(shapes):
    draw = {'A': 'X', 'B': 'Y', 'C': 'Z' }
    playerWins = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    playerLooses = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    s1, instruction = shapes[0], shapes[2]
    s2 = ''
    # Draw
    if instruction == 'Y':
        s2 = draw[s1]
    # Loose
    elif instruction == 'X':
        s2 = playerLooses[s1]
    else:
        s2 = playerWins[s1]
    return s1 + " " + s2

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("too few arguments")
    else:
        file = sys.argv[1]
        if not os.path.isfile(file):
            print(file, "does not exist.")
        else:
            score(file)