from collections import Counter
import sys
n = int(input())
l = []

for _ in range(n):
    num = int(sys.stdin.readline())
    l.append(num)
l.sort()

cnt = Counter(l)
answer = cnt.most_common()
print(answer[0][0])