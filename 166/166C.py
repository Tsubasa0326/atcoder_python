[N,M] = [int(s) for s in input().rstrip().split(' ')]
L_H = [int(s) for s in input().rstrip().split(' ')]
L_map = [0]*N
for i in range(M):
    [A_i,B_i] = [int(s) for s in input().rstrip().split(' ')]
    L_map[A_i-1] = max(L_map[A_i-1],L_H[B_i-1])
    L_map[B_i-1] = max(L_map[B_i-1],L_H[A_i-1])
ans = 0
for n in range(N):
    if L_map[n] == 0:
        ans += 1
    else:
        if L_H[n] > L_map[n]:
            ans += 1
print(ans)
