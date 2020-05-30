X = int(input())
k = 100
ans = 0
while k < X:
    ans += 1
    k = int(k*1.01)
print(ans)