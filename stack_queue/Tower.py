#https://programmers.co.kr/learn/courses/30/lessons/42588
heights = [5,4,3,2,1]
answer = []

#answer = [0] * len(heights)
for i in range(0,len(heights)):
    answer.append(0)

for i in range(len(heights)-1,-1,-1):    
    for j in range(i-1, -1, -1):
        if heights[i] < heights[j]:
            answer[i] = j + 1
            break

print(answer)