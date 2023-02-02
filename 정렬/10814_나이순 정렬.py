# 문제
# 온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 온라인 저지 회원의 수 N이 주어진다. (1 ≤ N ≤ 100,000)

# 둘째 줄부터 N개의 줄에는 각 회원의 나이와 이름이 공백으로 구분되어 주어진다. 나이는 1보다 크거나 같으며, 200보다 작거나 같은 정수이고, 이름은 알파벳 대소문자로 이루어져 있고, 길이가 100보다 작거나 같은 문자열이다. 입력은 가입한 순서로 주어진다.

# 출력
# 첫째 줄부터 총 N개의 줄에 걸쳐 온라인 저지 회원을 나이 순, 나이가 같으면 가입한 순으로 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력한다.

import sys
# 온라인 저지 회원의 수 n 입력
n = int(input())
# 나중에 리스트에 받아 정렬할 것이므로 빈 리스트를 생성해둔다.
l = []
# 회원마다 정보를 입력해야 하므로 회원수만큼 정보를 받아준다.
for _ in range(n):
    # input 대신 sys.stdin.readline()을 사용해 시간복잡도를 낮춰준다.
    age, name = map(str, sys.stdin.readline().split())
    # 빈 리스트 l에 리스트 형태로 age, name을 넣어준다. 리스트 형태로 하지 않으면 정렬할 때 age, name의 쌍이 뒤죽박죽 될 수 있기 때문에 리스트 형태로 받는다.
    l.append([int(age), name])
# 나이를 기준으로 오름차순하여 정렬하므로 key = lambda x:x[0]을 이용한다. 나이가 리스트에서 0에 해당하는 위치에 있으므로 0을 사용한다.
l.sort(key = lambda x: x[0])
# 정렬이 된 리스트들의 리스트에서 값을 꺼내 출력한다.
for i in l:
    print(i[0],i[1])