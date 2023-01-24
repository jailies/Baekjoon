k, n = map(int, input().split())
l = []
for _ in range(k):
    l.append(int(input()))
start, end = 1, max(l) # 이진 탐색의 처음과 끝 위치

while start <= end:
    mid = (start + end) // 2
    lines = 0
    # 모든 랜선값을 mid로 나누어 총 몇개의 랜선이 나오는지 확인하고 lines의 개수로 할당한다.
    for i in l:
        lines += i // mid
    # 랜선의 개수가 목표치 이상이면 mid+1을 start로 두고 다시  while문을 반복한다.
    if lines >= n:
        start = mid + 1
    # 랜선의 개수가 목표치 이하면 mid-1을 end로 두고 다시 while문을 반복한다.
    else:
        end = mid - 1
# start와 end가 같아지면, 즉 조건을 만족하는 최대의 랜선길이를 찾으면 while문을 탈출하고 결과값 end를 출력한다.
print(end)