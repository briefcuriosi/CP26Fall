#Submit to CCC '13 J2 - Rotating letters

# 1
# Word = input()
# letters = "IOSHZXN"
# answer = "Yes"
# for i in range (len(Word)):
#     if Word[i] not in letters:
#         answer = ("NO")
# print(answer)

# 2
# s = input()
# a = s.count("I") + s.count("O") + s.count("S") + s.count("H") + s.count("Z") + s.count("X") + s.count("N")
# if a == len(s):
#     print("YES")
# else:
#     print("NO")

# CCC '18 J2 - Occupy parking

# 1
number = int(input())
yesterday = input()
today = input()

count = 0
for i in range(number):
    if yesterday[i] == 'C' and today[i]:
        count += 1
print(count)


