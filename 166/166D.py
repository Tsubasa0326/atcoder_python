X = int(input())
k = 0
for a in range(151):
    for b in range(-150,150):
        if X == a**5 - b**5:
            print("{} {}".format(a,b))
            k = 1
            break
    if k == 1:
        break



