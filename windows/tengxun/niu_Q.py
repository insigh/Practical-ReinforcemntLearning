"""
7 14
"""

# QQ, Niuniu = list(map(int, input().strip().split()))
# print(QQ, Niuniu)
QQ = 7
Niuniu = 14
def dfs(x, y, x_win, y_win, step, solution):
    if x+step == QQ and y == Niuniu:
        solution.append((x_win+[step], y_win))
        return
    if x == QQ and y+step == Niuniu:
        solution.append((x_win, y_win+[step]))
        return
    if x > QQ or y > Niuniu:
        return
    if x < QQ:
        dfs(x+step, y, x_win+[step], y_win, step+1, solution)
    if y < Niuniu:
        dfs(x, y+step, x_win, y_win+[step], step+1, solution)


solution = []
dfs(0, 0, [], [], 1, solution)
print(solution)
solution.sort(key=lambda x:len(x[0]))
print(solution)
print(len(solution[0][0])) if solution else print(-1)