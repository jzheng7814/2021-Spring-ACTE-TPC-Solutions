N, K = [int(i) for i in input().split()]
mp = {}

for i in range(N):
    args = input().split()
    mp[args[0]] = args[1]

for i in range(K):
    print(mp[input()])