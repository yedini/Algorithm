n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))

result = price[0] * dist[0]
oil = price[0]  # 현재 주유소 가격

for i in range(1, len(dist)):
    if oil*dist[i] <= price[i]*dist[i]:
        result += oil*dist[i]
    else:
        result += price[i]*dist[i]
        oil = price[i]

print(result)