[S,W] = [int(s) for s in input().rstrip().split(' ')]
if W >= S:
    print("unsafe")
else:
    print("safe")