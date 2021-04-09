def dfs(mp, loc, visit, canReach, traveled, maxDist):
    if visit[loc] == True or traveled > maxDist:
        return

    visit[loc] = True
    canReach.append(loc)
    for i, j in mp[loc]:
        dfs(mp, i, visit, canReach, traveled + j, maxDist)

N, K = [int(i) for i in input().split()]
m = {}

for i in range(K):
    start, end, weight = input().split()
    weight = int(weight)
    
    if start not in m:
        m[start] = []
    
    if end not in m:
        m[end] = []
    
    m[start].append((end, weight))
    m[end].append((start, weight))

visited = {i:False for i in m.keys()}
reached_cities = []
dfs(m, 'A', visited, reached_cities, 0, N)

reached_cities = sorted(reached_cities)
for i in reached_cities[1:]:
    print(i)
