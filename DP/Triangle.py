import unittest

# solution의 매개변수를 global로 사용하지 않기
triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

def solution(triangle):
    for i in range(len(triangle)-1):
        triangle[i + 1][0] += triangle[i][0]
        triangle[i + 1][-1] += triangle[i][-1]
        for j in range(1, len(triangle[i])):  
            triangle[i+1][j] += max(triangle[i][j-1], triangle[i][j])
    return max(triangle[-1])

class SolutionTests(unittest.TestCase):
    def test_runs(self):
        solution(triangle)
    
    def test(self):
        self.assertEqual(solution(triangle),30)

if __name__=="__main__":
    unittest.main()
    print(solution(triangle))