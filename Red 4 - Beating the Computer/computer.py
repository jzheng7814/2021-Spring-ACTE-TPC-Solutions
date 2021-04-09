from math import ceil

N = int(input())
blocks = [int(input()) for i in range(N)]
elim = set()

for i in blocks:
    if i in elim:
        elim.remove(i)
    else:
        elim.add(i)

for i in elim:
    blocks.remove(i)

if len(elim) == 1:
    for i in elim:
        blockLength = int(ceil((float) (i - 2) / 2.0))
        blocks.append(blockLength)
        blocks.append(blockLength)
else:
    elements = sorted(list(elim))
    blocks.append(elements[0])
    blocks.append(elements[0])

print(*sorted(blocks), sep = '\n')