[A,B,C,D] = [int(s) for s in input().rstrip().split(' ')]
t = -(-A//D)
a = -(-C//B)
if t >= a:
    print("Yes")
else:
    print("No")