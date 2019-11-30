#https://programmers.co.kr/learn/courses/30/lessons/42746
numbers = [6,10,2]

numbers = list(map(str, numbers))
numbers.sort(key=lambda x:x*3, reverse = True)

#str(int(''.join(numbers)))
if sum(list(map(int,numbers))) == 0:
    numbers = list(set(numbers))
print(''.join(numbers))