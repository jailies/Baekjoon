n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))

l.sort(reverse=True)
result = []

for i in range(n):
    result.append(l[i] * (i+1))
print(max(result))