n, m, l = map(int, input().split())
stations = list(map(int, input().split()))
# 휴게소 리스트에 출발지점 0과 도착지점 l을 추가해주고 정렬한다.
stations.append(0)
stations.append(l)
stations.sort()

# 고속도로 끝에는 휴게소를 설치할 수 없기에 마지막 지점을 l-1로 지정해준다.
start, end = 1, l-1

while start <= end:
    count = 0
    # 가장 멀리 떨어져 있는 휴게소 사이 거리
    mid = (start+end) // 2
    for i in range(1, len(stations)):
        if stations[i] - stations[i-1] > mid:
            # 나눈 만큼 휴게소를 설치하는데, 현재 설치된 구역은 제외하므로 -1을 해준다.
            count += (stations[i] - stations[i-1] -1) // mid
    if count > m:
        start = mid + 1
    else:
        end = mid -1
        answer = mid

print(answer)