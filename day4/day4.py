from aoc_helper import truncate_newline

def main(fileName):
    with open(fileName) as fd:
        overlapCount = 0
        for line in fd:
            line = truncate_newline(line)
            r1, r2 = line.split(',', 2)
            overlapCount += 1 if overlap(r1, r2) else 0
            print(r1, "and", r2, ":", overlap(r1, r2))
        print("overlapping sections:", overlapCount)

# Part 1
def containedIn(r1, r2) -> bool:
    r1l, r1u = [int(n) for n in r1.split("-", 2)]
    r2l, r2u = [int(n) for n in r2.split("-", 2)]
    if (r1l >= r2l and r1u <= r2u) or (r2l >= r1l and r2u <= r1u):
        return True
    return False

# Part 2
def overlap(r1, r2) -> bool:
    r1l, r1u = [int(n) for n in r1.split("-", 2)]
    r2l, r2u = [int(n) for n in r2.split("-", 2)]
    if r2l <= r1u <= r2u or r2l <= r1l <= r2u or r1l <= r2u <= r1u or r1l <= r2l <= r1u:
        return True
    return False

if __name__ == '__main__':
    main("input.txt")