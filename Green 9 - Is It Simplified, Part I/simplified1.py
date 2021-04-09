N = int(input())

for k, l in [[int(j) for j in input().split()] for i in range(N)]:
    if k % l == 0:
        print('F')
    else:
        print('T')