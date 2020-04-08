import unittest
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

class SolutionTests(unittest.TestCase):
    def test_runs(self):
        solution([1,2,3,9,10,12],7)
    
    def test(self):
        self.assertEqual(solution([1,2,3,9,10,12],7),2)

if __name__=="__main__":
    unittest.main()
    print(solution(scoville, K))