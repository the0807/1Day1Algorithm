# 10811번 "바구니 뒤집기"

n, m = map(int, input().split())

basket = [i for i in range(1, n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp

for i in range(n):
    print(basket[i], end=" ")