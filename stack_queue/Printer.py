#https://programmers.co.kr/learn/courses/30/lessons/42587

priorities = [1, 1, 9, 1, 1, 1]
location = 0
answer = 0

enum = list(enumerate(priorities))
loca = enum[location]

while loca in enum:
    m = max(enum, key = lambda x : x[1])
    a = enum.pop(0)
    if a[1] < m[1]:
        enum.append(a)
    else:
        answer+=1

print(answer)