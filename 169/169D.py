N = int(input())
L_P = []
num = N
ans = 0
if N == 1:
    print(ans)
else:
    for i in range(2,int(-(-num**0.5//1))+1):
        if num % i == 0:
            cnt = 0
            while num % i == 0:
                cnt += 1
                num //= i
            L_P.append(cnt)
        if num == 1:
            break
    else:
        L_P.append(1)
    for x in L_P:
        for i in range(1,100):
            if i*(i+1)//2 > x:
                ans += i-1
                break
    print(ans)      