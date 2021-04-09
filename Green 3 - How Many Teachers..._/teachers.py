N, K = [int(i) for i in input().split()]
K_i = []

for i in range(K):
    K_i.append(int(input()))

total = 0
for i, j in enumerate(sorted(K_i, reverse=True)):
    if total >= N:
        print(i)
        break
    total += j