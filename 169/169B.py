N = int(input())
L_A = [int(s) for s in input().rstrip().split(' ')]
if 0 in L_A:
    print(0)
else:
    k = 1
    for i in range(N):
        k *= L_A[i]
        if k > 10**18:
            print("-1")
    else:
        print(k)
            