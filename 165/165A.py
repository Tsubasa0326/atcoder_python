K = int(input())
[A,B]= [int(s) for s in input().rstrip().split(' ')]
[a_1,a_2] = [A//K,A%K]
[b_1,b_2] = [B//K,B%K]
if a_1 != b_1:
    print("OK")
else:
    if a_2==0 or b_2==0:
        print("OK")
    else:
        print("NG")