# 도시 수
n = int(input())
# 도시와 도시 사이의 거리
distance = list(map(int, input().split()))
# 주유소의 리터당 가격
price = list(map(int, input().split()))

# 결괏값 초기화
result = 0

# 첫번째 주유소 
min_price = price[0]

for i in range(n-1):
    if min_price > price[i]:
        min_price = price[i]
    result += min_price * distance[i]

print(result)