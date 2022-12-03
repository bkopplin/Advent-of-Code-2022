def main():
    with open("input.txt") as fd:
        totalPriority = 0
        for line in fd:
            line = truncate_newline(line)
            compSize = int(line.__len__()/2)
            comp1 = line[0:compSize]
            comp2 = line[compSize:]
            # It is safe to assume that there is exactly one duplicated item in each compartment
            item = duplicatedItem(comp1, comp2)
            totalPriority += itemToPriority(item)
        print("total priority:", totalPriority)

def groupPriority():
    with open("input.txt") as fd:
        groups = [None] * 3
        i = 0
        totalPriority = 0
        for line in fd:
            groups[i] = truncate_newline(line)
            i += 1
            # Get the badge once we have three groups
            if i == 3:
                badge = getBadge(groups)
                totalPriority += itemToPriority(badge)
                i = 0
        print("total priority for badges:", totalPriority)

def getBadge(groups):
    for i in groups[0]:
        for j in groups[1]:
            for k in groups[2]:
                if i == j == k:
                    return i

def truncate_newline(line):
    return line[:-1] if line[-1] == '\n' else line

def duplicatedItem(comp1, comp2):
    for char1 in comp1:
        for char2 in comp2:
            if char1 == char2:
                return char1

def itemToPriority(item):
    # compute separately for uppercase and lowercase
    if ord(item) >= 97:
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27

if __name__ == '__main__':
    groupPriority()

