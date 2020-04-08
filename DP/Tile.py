import unittest

N = 6

def solution(N):
    lists = [1,1,]
    for i in range(N):
        lists.append(lists[i]+lists[i+1])
    return lists[-1]*2

class SolutionTests(unittest.TestCase):
    def test_runs(self):
        solution(N)
    
    def test(self):
        self.assertEqual(solution(N),26)

if __name__=="__main__":
    #unittest.main()
    print(solution(N))