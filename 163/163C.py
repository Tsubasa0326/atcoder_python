N = int(input())
L = [int(s) for s in input().rstrip().split(' ')]
L_0 = [0 for i in range(N)]
for x in L:
    L_0[x-1] += 1
for y in L_0:
    print(y)