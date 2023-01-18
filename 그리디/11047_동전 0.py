n, k = map(int, input().split())
v = []

for i in range(n):
    v.append(int(input()))

v.sort(reverse=True)

answer = 0

for coin in v:
    if k >= coin:
        answer += k//coin
        k %= coin
        if k == 0:
            break

print(answer)