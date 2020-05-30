[N,M] = [int(s) for s in input().rstrip().split(' ')]
if M == 1:
    print("1 2")
else:
    for i in range(1,M//2+1):
        print("{} {}".format(i,M+1-i))
    for i in range(1,-(-M//2)+1):
        print("{} {}".format(M+i,2*M+2-i))
