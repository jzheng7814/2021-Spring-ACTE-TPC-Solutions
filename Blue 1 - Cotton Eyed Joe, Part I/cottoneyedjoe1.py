def dfs(mp, loc, visit, canReach):
    if visit[loc] == True:
        return

    visit[loc] = True
    canReach.append(loc)
    for i in mp[loc]:
        dfs(mp, i, visit, canReach)

N = int(input())
m = {}

for i in range(N):
    start, end = input().split()
    
    if start not in m:
        m[start] = []
    
    if end not in m:
        m[end] = []
    
    m[start].append(end)
    m[end].append(start)

visited = {i:False for i in m.keys()}
reached_cities = []
dfs(m, 'A', visited, reached_cities)

reached_cities = sorted(reached_cities)
for i in reached_cities[1:]:
    print(i)
