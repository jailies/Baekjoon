# 문제
# 수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

# Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표의 개수와 같아야 한다.

# X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.

# 입력
# 첫째 줄에 N이 주어진다.

# 둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.

# 출력
# 첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.
import sys
n = int(input())
xnlist = list(map(int, sys.stdin.readline().split()))
l = xnlist
xnset = set(xnlist)
xnlist = list(xnset)
xnlist.sort()

# dict[요소]: 요소의 index 형태로 저장해 준다.
dic = {xnlist[i]: i for i in range(len(xnlist))}

for x in l:
    # print(xnlist.index(x), end=' ') 
    # list.index는 시간복잡도가 O(n)
    print(dic[x], end =' ')