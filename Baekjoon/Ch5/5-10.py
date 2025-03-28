# 5622번 "다이얼"

num_dict = {"ABC":3, "DEF":4, "GHI":5, "JKL":6, "MNO":7, "PQRS":8, "TUV":9, "WXYZ":10}

string = input()
time = 0

for i in string:
    for j, k in num_dict.items():
        if i in j:
            time += k
print(time)