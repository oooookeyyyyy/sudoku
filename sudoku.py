def check(line, column):
    def _(i):
        if column//3 == 0:
            if n not in [table[i][j] for j in range(3)]:
                return 1
        elif column//3 == 1:
            if n not in [table[i][j] for j in range(3, 6)]:
                return 1
        elif n not in [table[i][j] for j in range(6, 9)]:
            return 1
        return 0

    for n in range(1 if table[line][column] is None else table[line][column]+1, 10):
        if n not in table[line] and n not in [table[i][column] for i in range(9)]:
            no = 0
            if line//3 == 0:
                for i in range(3):
                    no += _(i)
            elif line//3 == 1:
                for i in range(3, 6):
                    no += _(i)
            else:
                for i in range(6, 9):
                    no += _(i)
            if no == 3:
                return n
    table[line][column] = None
    return

table = [[None,None,7,None,None,5,9,None,None], [None,None,1,8,9,None,None,2,None], [None,None,4,None,None,None,None,None,None], [None,None,None,None,None,None,2,None,None], [None,4,None,7,None,None,None,6,None], [None,None,None,None,None,6,None,1,5], [6,7,None,None,None,1,None,None,8], [None,None,None,None,6,None,None,None,None], [None,9,5,3,8,None,None,None,None]]
stack = []
line = 0
while line < 9:
    column = 0
    while column < 9:
        if table[line][column] is None:
            while True:
                if CHECK := check(line, column):
                    table[line][column] = CHECK
                    stack.append((line, column))
                    break
                else:
                    prev = stack.pop()
                    line, column = prev[0], prev[1]
        column += 1
    line += 1
for line in table:
    print(line)
