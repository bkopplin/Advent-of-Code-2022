def main(fileName):
  with open(fileName) as fd:
    stacks = {}
    # read in stack
    for line in fd:
      if line == "\n":
        break
      for i in range(1, len(line), 4):
        pos = str(int((i-1)/4+1))
        if not pos in stacks:
          stacks[pos] = []
        # Only add if the current character is a letter, that means don't add white space or numbers
        if not line[i] == ' ' and not ord(line[i]) <= 57:
          stacks[pos].insert(0, line[i])

    print(stacks)
    # move crates around
    for line in fd:
      _, qty, _, frm, _, to = line.split(' ')
      qty = int(qty)
      to = to.rstrip()

      # CrateMover 9000
      # for step in range(0, qty):
      #   stacks[to].append(stacks[frm].pop())

      # CrateMover 9001
      stacks[to] = stacks[to] + stacks[frm][-qty:]
      del stacks[frm][-qty:]

      print(qty, frm, to)
    print(stacks)

    msg = ""
    # get message
    for i in range(0, len(stacks.keys())):
      msg = msg + stacks[str(i+1)][-1]
    print(msg)


if __name__ == '__main__':
  main("input.txt")
