def dfs(solutions, temp_solution):
    def grid():
        return [[-1 if len(temp_solution)<=i else 1 if temp_solution[i]==j else 0 for j in range(8)] for i in range(8)]

    if len(temp_solution)==8:
        solutions.append(list(temp_solution))
        yield [[2 if temp_solution[i]==j else 0 for j in range(8)] for i in range(8)]
        return
    def check(temp_solution, col):
        row = len(temp_solution)
        b = True
        for i,v in enumerate(temp_solution):
            b &= (v != col and abs(row-i)!=abs(col-v))
        return b

    for i in range(8):
        if check(temp_solution, i):
            temp_solution.append(i)
            yield grid()
            yield from dfs(solutions, temp_solution)
            temp_solution.pop()
        else:
            g = grid()
            g[len(temp_solution)][i] = 3
            yield g

