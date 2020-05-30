import itertools
n, m, q = map(int, input().split())
lst = [0] * q
for i in range(q):
    a, b, c, d = map(int, input().split())
    lst[i] = (a, b, c, d)
L = list(itertools.combinations_with_replacement(range(1,m+1), n))
ans = 0 
for l in L:
    point_l = 0
    for rule in lst:
        if l[rule[1]-1]-l[rule[0]-1] == rule[2]:
            point_l += rule[3]
    ans = max(ans,point_l)
print(ans)