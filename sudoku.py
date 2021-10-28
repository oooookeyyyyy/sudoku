def check(line, column):
    for n in range(1 if table[line][column] is None else table[line][column]+1, 10):
        if n not in table[line]:
            if n not in [table[i][column] for i in range(9)]:
                no = 0
                if line//3 == 0:
                    if column//3 == 0:
                        for i in range(3):
                            if n not in [table[i][j] for j in range(3)] :
                                no += 1
                        if no == 3:
                            return n
                    elif column//3 == 1:
                        for i in range(3):
                            if n not in [table[i][j] for j in range(3, 6)] :
                                no += 1
                        if no == 3:
                            return n
                    else:
                        for i in range(3):
                            if n not in [table[i][j] for j in range(6, 9)] :
                                no += 1
                        if no == 3:
                            return n
                elif line//3 == 1:
                    if column//3 == 0:
                        for i in range(3, 6):
                            if n not in [table[i][j] for j in range(3)] :
                                no += 1
                        if no == 3:
                            return n
                    elif column//3 == 1:
                        for i in range(3, 6):
                            if n not in [table[i][j] for j in range(3, 6)] :
                                no += 1
                        if no == 3:
                            return n
                    else:
                        for i in range(3, 6):
                            if n not in [table[i][j] for j in range(6, 9)] :
                                no += 1
                        if no == 3:
                            return n
                else:
                    if column//3 == 0:
                        for i in range(6, 9):
                            if n not in [table[i][j] for j in range(3)] :
                                no += 1
                        if no == 3:
                            return n
                    elif column//3 == 1:
                        for i in range(6, 9):
                            if n not in [table[i][j] for j in range(3, 6)] :
                                no += 1
                        if no == 3:
                            return n
                    else:
                        for i in range(6, 9):
                            if n not in [table[i][j] for j in range(6, 9)] :
                                no += 1
                        if no == 3:
                            return n
    table[line][column] = None
    return

table = input('input table')# [[None,None,7,None,None,5,9,None,None], [None,None,1,8,9,None,None,2,None], [None,None,4,None,None,None,None,None,None], [None,None,None,None,None,None,2,None,None], [None,4,None,7,None,None,None,6,None], [None,None,None,None,None,6,None,1,5], [6,7,None,None,None,1,None,None,8], [None,None,None,None,6,None,None,None,None], [None,9,5,3,8,None,None,None,None]]
stack = []
line = 0
while line < 9:
    column = 0
    while column < 9:
        if table[line][column] is None:
            while True:
                CHECK = check(line, column)
                if CHECK:
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