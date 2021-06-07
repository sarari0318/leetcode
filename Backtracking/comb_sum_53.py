class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates = sorted(candidates)
        res = []
        self.backtracking(res, candidates, target, [], 0)
        return res
        
        
    def backtracking(self, res, candidates, target, comb, start):
        
        for i in range(start, len(candidates)):
            if candidates[i] == target:
                comb.append(candidates[i])
                res.append(list(comb))
            else:
                if candidates[i] > target:
                    break
                comb.append(candidates[i])
                self.backtracking(res, candidates, target - candidates[i], comb, i)
            comb.pop()


        '''
        流れ
        
        res = []
        2, 2, 2, 2 > 7
                 終 3, 6, 7
        
        2, 2, 3 == 7 ⇨ res.append([2, 2, 3])
              終 6, 7
        
        2, 2, 6 > 7
              終 7 
        
        2, 3, 3 > 7
              終 6, 7
            
        2, 6 > 7
           終 7
            
        3, 3, 3 > 7
              終 6, 7
        
        3, 6 > 7
           終 7
            
        6, 6 > 7
           終 7
            
        7 == 7 ⇨ res.qppend([7])
        '''