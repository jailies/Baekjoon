n, m, v = map(int, input().split())
l = []
for i in range(m):
    l.append(list(map(int, input().split())))
# dfs 메서드 정의
def dfs(graph, v, visited):
	# 현재 노드를 방문 처리
	visited[v] = True
	print(v, end='')
	# 현재 노드와 연결된 노드를 재귀적으로 방문
	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)

visited = [False] * 9

dfs(l, 1, visited)