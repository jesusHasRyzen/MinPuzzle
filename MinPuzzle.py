dr = [-1, +1, 0, 0]
dc = [0, 0, -1, +1]
def minEffort(puzzle):
    start = [0,0]
    tempRowCount = len(puzzle)
    # print(tempRowCount)
    tempColumnCount = len(puzzle[1])
    end = [tempRowCount-1,tempColumnCount-1]
    effort = 0
    path = []
    path.append(start)
    # print(puzzle[0][0])
    print("init helper, start  0 , 0 end")

    print("cell is = ", puzzle[0][0])

    effort = helper(puzzle, start, end, path, effort)
    print(path)
    return effort
def helper(puzzle, start, end, path, effort):
    if start == end :
        return effort
    rLength = len(puzzle)
    cLength = len(puzzle[1])
    currentR = start[0]
    currentC = start[1]
    # if currentC >=rLength or currentR >=rLength:
        # return
    for i in range(4):
        newR = currentR + dr[i]
        newC = currentC + dc[i]
        if newC < 0 or newR < 0:
            continue
        if newC >= cLength or newR >= rLength:
            continue
        if [newR,newC] not in path:
            path.append([newR,newC])
            # print(puzzle[0][0])
            print("init helper, start ", newR, ",", newC, " end = ", end)

            print("cell is = ",puzzle[newR][newC])
            if effort < abs(puzzle[currentR][currentC] - puzzle[newR][newC]):
                effort = abs(puzzle[currentR][currentC] - puzzle[newR][newC])
                helper(puzzle,[newR,newC], end, path, effort)
    return effort




puzzle = [[1, 3, 5], [2, 8, 3], [3, 4, 5]]
print(minEffort(puzzle))
