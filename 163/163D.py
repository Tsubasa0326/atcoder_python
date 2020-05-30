"""
大きな勘違い
p = 226732710 #10***100 %(10**9+7)
num = 10**9+7
[N,K] = [int(s) for s in input().rstrip().split(' ')]
L = []
ans = 0
for i in range(K,N+2):
    p_i = p*K % num
    a_i = (p_i + i*(i-1)//2) % num
    b_i = a_i + i*(N-i+1)
    if i*(N-i+1) >= 10**9+6:
        ans = 10**9+7
        break
    else:
        if b_i >= num:
            L_i = [[0,b_i % num],[a_i,10**9+6]]
        else:
            L_i = [[a_i,b_i]]
        for x in L_i:
            for y in L:
                if x[1] >= y[0] and y[1] >= x[0]:
                    y[0] = min(x[0],y[0])
                    y[1] = max(x[1],y[1])
                    break
            else:
                L.append(x)
        for y in L:
            ans += y[1]-y[0]+1
print(ans)
"""
p = 226732710 #10***100 %(10**9+7)
num = 10**9+7
[N,K] = [int(s) for s in input().rstrip().split(' ')]
L = []
ans = 0
for i in range(K,N+2):
    ans += i*(N-i+1)+1
    ans %= num
print(ans)