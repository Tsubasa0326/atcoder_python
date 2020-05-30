# by Ebich
N = int(input())
A = list(map(int, input().split()))
ans = 0
"""
A[i] + A[j] = j - i
<=> A[i] + i = j - A[j]
"""
L_i = [A[i] + i for i in range(N)]
L_j = [j - A[j] for j in range(N)]
# L_j[x] < x <= 2 * (10**5)
ans_lis = [0] * (2*(10**5))
for x in L_i:
    if x < 2*(10**5):
        ans_lis[x-1] += 1
for y in L_j:
    if y > 0:
        ans += ans_lis[y-1]
print(ans)