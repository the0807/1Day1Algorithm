# 1316번 "그룹 단어 체커"

n = int(input())

for i in range(n):
    word = input()
    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            n -= 1
            break

print(n)