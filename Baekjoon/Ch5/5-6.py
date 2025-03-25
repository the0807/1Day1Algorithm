# 10809번 "알파벳 찾기"

s = input()
abc = "abcdefghijklmnopqrstuvwxyz"

for i in abc:
    print(s.find(i), end = ' ')