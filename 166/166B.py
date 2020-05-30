[N,K] = [int(s) for s in input().rstrip().split(' ')]
L = [0]*N
for i in range(K):
    d_i = int(input())
    A_i = [int(s) for s in input().rstrip().split(' ')]
    for a_i in A_i:
        L[a_i-1] += 1
print(L.count(0))