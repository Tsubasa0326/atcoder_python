S = input()
a = len(S)
mod = 0
ten = 1
L = [0]*2019 #余りの列
L[0] = 1
for i in range(a-1,-1,-1):
    mod = (int(S[i])*(ten)+mod) %2019
    L[mod] += 1
    ten = (ten*10)%2019
ans = 0
for i in L:
  ans += i*(i-1)//2
print(ans)