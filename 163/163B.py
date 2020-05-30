[N,M] = [int(s) for s in input().rstrip().split(' ')]
L = [int(s) for s in input().rstrip().split(' ')]
S = sum(L)
if N >= S:
    print(N-S)
else:
    print("-1")