n = int(input())
l =[]
for _ in range(n):
    arrive, test = map(int,input().split())
    l.append([arrive, test])
l.sort(key = lambda x:x[0])

time = 0
for i in l:
    if time <i[0]:
        time = i[0] + i[1]
    else:
        time += i[1]
print(time)