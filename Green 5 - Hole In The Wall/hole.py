N, K = [int(i) for i in input().split()]
lines = [input() for i in range(N)]

for i in lines:
    for k in [int(j) for j in i.split()]:
        if k == 1:
            print(0, end = ' ')
        else:
            print(1, end = ' ')
    print()