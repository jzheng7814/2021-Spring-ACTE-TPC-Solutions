def dfs(i, j, visit, grd):
    if visit[i][j] or grd[i][j] != 1:
        return
    
    visit[i][j] = True
    dfs(i - 1, j, visit, grd)
    dfs(i + 1, j, visit, grd)
    dfs(i, j + 1, visit, grd)
    dfs(i, j - 1, visit, grd)
    

N = int(input())
grid = [[0] + [int(i) for i in input().split()] + [0] for j in range(N)]
visited = [[False for i in range(N + 2)] for j in range(N + 2)]
count = 0

grid.append([0 for i in range(N + 2)])
grid.insert(0, [0 for i in range(N + 2)])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if grid[i][j] == 1 and not visited[i][j]:
            count += 1
            dfs(i, j, visited, grid)

print(count)