N, K = [int(i) for i in input().split()]
bookAndSubject = []

for i in range(K):
    input()

for i in range(N):
    bookAndSubject.append(input().rsplit(' ', 1))

print(*[i[0] for i in sorted(sorted(bookAndSubject, key = lambda i: i[0]), key = lambda i: i[1])], sep = '\n')