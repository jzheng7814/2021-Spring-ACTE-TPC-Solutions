bottomLeft1 = [int(i) for i in input().split()]
topRight1 = [int(i) for i in input().split()]
bottomLeft2 = [int(i) for i in input().split()]
topRight2 = [int(i) for i in input().split()]

length1 = topRight1[0] - bottomLeft1[0]
width1 = topRight1[1] - bottomLeft1[1]
length2 = topRight2[0] - bottomLeft2[0]
width2 = topRight2[1] - bottomLeft2[1]
overlappingLength = topRight1[0] - bottomLeft2[0]
overlappingWidth = topRight1[1] - bottomLeft2[1]

print(length1 * width1 + length2 * width2 - overlappingLength * overlappingWidth)