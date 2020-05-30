import sys
N = int(sys.stdin.readline())
data = sys.stdin.readlines()
L = [x.strip("\n") for x in data]
print(len(list(set(L))))