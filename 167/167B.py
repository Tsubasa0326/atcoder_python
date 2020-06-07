[A,B,C,K] = [int(s) for s in input().rstrip().split(' ')]
ans = 0
if K <= A:
    ans = K
else:
    ans += A
    if K > A+B:
        ans -= K-A-B
print(ans)