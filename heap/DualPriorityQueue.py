import heapq

def solution(operations):
    heap = []
    for i in operations:
        arr = i.split(' ')
        if arr[0]=='I':
            heapq.heappush(heap,int(arr[1]))
        else: # case D
            if heap:
                if arr[1]=='-1':
                    'ssss',heapq.heappop(heap)
                else: # case D 1
                    heap.remove(max(heap))
    answer = []

    if heap:
        answer.append(max(heap))
        answer.append(min(heap))        
    else:
        answer=[0,0]
    
    return answer

if __name__=="__main__":
    input = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    print(solution(input))