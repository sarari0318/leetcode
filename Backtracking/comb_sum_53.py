class Solution:
    def combinationSum(self, candidates, target):

        '''
         Parameters
        ----------
            candidates: List[int]
            target: int 
        Returns
        -------
            res: List[List[int]]
            ⇨ return a list of all unique combinations of candidates where the chosen numbers sum to target.
        '''
        
        # candidatesをソート化
        candidates.sort()
        res = []
        self.backtracking(res, candidates, target, [], 0)
        return res
        
        
    def backtracking(self, res, candidates, target, comb, start):
        
        for i in range(start, len(candidates)):
            # i番目の要素がtargetの値を超えてしまえば、break
            if candidates[i] > target:
                break
            # i番目の要素がtargetの値と等しければ、resにcombを追加
            elif candidates[i] == target:
                comb.append(candidates[i])
                res.append(list(comb))
            # i番目の要素がtargetの値より小さければ、
            else:
                # 引き続きcombに要素を追加し、その組み合わせの合計がtargetに等しくなるかチェック
                comb.append(candidates[i])
                self.backtracking(res, candidates, target - candidates[i], comb, i)
            comb.pop()
