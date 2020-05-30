N = int(input())
[a,b] = [N // 15,N % 15]
S = 60*a*a
if b == 0:
  print(S)
else:
  for i in range(1,b+1):
    if i % 3 != 0 and i % 5 != 0:
      S += 15*a+i
  print(S)