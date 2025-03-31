# 10988번 "팰린드롬인지 확인하기"

string = list(input())
string_reverse = reversed(string)

if list(string_reverse) == string:
    print(1)
else:
    print(0)