N, L = [int(i) for i in input().split()]
A = [int(input()) for i in range(N)]
B = [int(input()) for i in range(N)]
possiblities = set()

def simulate(day):
    if day == 0:
        possiblities.add((sum(A), sum(B)))
        return

    for i in range(len(A)):
        A_removed = A.pop(i)
        B.append(A_removed)

        for j in range(len(B)):
            B_removed = B.pop(j)
            A.append(B_removed)
            simulate(day - 1)
            A.pop()
            B.insert(j, B_removed)
        
        B.pop()
        A.insert(i, A_removed)

simulate(L)
print(len(possiblities))