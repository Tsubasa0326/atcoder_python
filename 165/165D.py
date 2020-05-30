[A,B,N] = [int(s) for s in input().rstrip().split(' ')]
if B == 1:
    print(0)
elif N < B:
    print(A*N//B)
else:
    print((A*(B-1))//B)