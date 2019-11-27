heights = [6,9,5,7,4]
answer = []
for i in range(len(heights)-1,-1,-1):
    if heights[i-1]>heights[i]:
        answer.insert(i,i)
    else:
        answer.insert(i,0)
print(answer)