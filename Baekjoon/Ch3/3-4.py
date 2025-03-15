# 25304번 "영수증"

total = int(input())
product_num = int(input())

total_price = 0
for i in range(product_num):
    price, num = map(int, input().split())

    total_price += price*num

if total == total_price:
    print('Yes')
else:
    print('No')