# 25314번 "코딩은 체육과목 입니다"

byte = int(input())

string = ''
for i in range(byte//4):
    string += 'long '

print(string + 'int')