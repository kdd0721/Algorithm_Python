#https://programmers.co.kr/learn/courses/30/lessons/42748?language=python3
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = []

for command in commands:
    answer.append(sorted(array[command[0]-1:command[1]])[command[2]-1])

print(answer)