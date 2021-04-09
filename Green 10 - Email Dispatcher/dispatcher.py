N = int(input())
counter = {}

for i in range(N):
    name = input()

    if name not in counter:
        counter[name] = 0
    
    counter[name] += 1

for i in sorted(counter.items(), key=lambda i: i[0]):
    print(*i)