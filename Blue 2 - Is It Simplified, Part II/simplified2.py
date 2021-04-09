N = int(input())
fractions = [[int(j) for j in input().split()] for i in range(N)]

for i in fractions:
    valid = True
    for j in range(2, i[1] + 1):
        if i[0] % j == 0 and i[1] % j == 0:
            valid = False
            break

    if valid:
        print('T')
    else:
        print('F')