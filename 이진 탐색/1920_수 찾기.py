# 첫째 줄에 N 받기
n = int(input())
# 다음 줄에 주어지는 N개의 정수
nl = list(map(int, input().split()))
# 다음 줄에 M 받기
m = int(input())
# 다음 줄에 주어지는 M개의 정수
ml = list(map(int, input().split()))
# 이진 탐색을 위해 nl을 정렬해준다.
nl.sort()

# 리스트 ml에 있는 수가 리스트 nl에 있는지 확인 하는 것이 문제의 목표이다.
# 확인을 할 때 시간 초과가 될 수 있으므로 이진 탐색을 이용하여 시간복잡도를 줄인다.

# 이진 탐색 소스코드 구현 (반복문)
def binary_search(nl, target, start, end):
	while start <= end:
		mid = (start + end) // 2
		# 찾은 경우 중간점 인덱스 반환
		if nl[mid] == target:
			return mid
		# 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
		elif nl[mid] > target:
			end = mid -1
		# 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
		elif nl[mid] < target:
			start = mid + 1
	return None

# 리스트 ml을 순회하며 target을 하나씩 꺼내면서 nl내에 있는지 이진탐색으로 확인하고,
# nl내에 target이 없다면 0을 출력, 있다면 1을 출력한다.
for target in ml:
    result = binary_search(nl, target, 0, n-1)
    if result == None:
    	print("0")
	else:
		print("1")