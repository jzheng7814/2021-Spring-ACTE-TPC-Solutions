N, K, L = [int(i) for i in input().split()]

for i in range(len(str(K))):
    if N * int(str(K)[:-i-1] + str(K)[-i:]) == L:
        print(i+1)

