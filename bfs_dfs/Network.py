#https://programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    answer = 0
    visit = []

    for i,j in enumerate(computers):
        if i not in visit:
            visit.append(i)
            dfs(visit, i, computers)
            answer+=1
    print(answer)
    return answer

def dfs(visit, start, computers):
    stack = []
    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
        for i,j in enumerate(computers):
            if computers[node][i]==1 and i not in visit:
                stack.append(i)

if __name__=="__main__":
    solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])