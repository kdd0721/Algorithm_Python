import heapq

scoville = [1,2,3,9,10,12]
K = 7

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)
    while K > scoville[0]:
        if len(scoville)==1 & K < scoville[0]:
            answer = -1
            break 

        heapq.heappush(scoville, heapq.heappop(scoville)+heapq.heappop(scoville)*2)
        answer+=1             
        
    return answer

if __name__=="__main__":
    print(solution(scoville, K))