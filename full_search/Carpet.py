#https://programmers.co.kr/learn/courses/30/lessons/42842

brown = 24
red = 24
answer = []

total = (brown+4)//2 #x+y
print(total)

for x in range(total-3,total//2,-1):
    y=total-x
    if (x-2)*(y-2)==red:
        answer = list([x,y])
        break;


print(answer)
