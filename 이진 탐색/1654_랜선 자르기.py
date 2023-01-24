k, n = map(int, input().split())
l = []
for _ in range(k):
    l.append(int(input()))
start, end = 1, max(l) # 이진 탐색의 처음과 끝 위치

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in l:
        lines += i // mid
    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)