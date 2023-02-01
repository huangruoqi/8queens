import sys

def dfs(n, solutions, temp_solution):
    if len(temp_solution)==n:
        solutions.append(list(temp_solution))
        return
    def check(temp_solution, col):
        row = len(temp_solution)
        b = True
        for i,v in enumerate(temp_solution):
            b &= (v != col and abs(row-i)!=abs(col-v))
        return b

    for i in range(n):
        if check(temp_solution, i):
            temp_solution.append(i)
            dfs(solutions, temp_solution)
            temp_solution.pop()

if __name__ == '__main__':
    n = sys.argv[0]
    solutions = []
    dfs(solutions, [], n)
    print(len(solutions))