class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        '''
         Parameters
        ----------
            n: int 
        Returns
        -------
            res: List[str]
            ⇨ return all combinations of well-formed parentheses.

        '''
        
        res = []
        self.backtracking(res, n, [], 0, 0)
        return res
    
    def backtracking(self, res, n, comb, left, right):
        
        if len(comb) == 2 * n:
            res.append(''.join(comb))
            
        # 左括弧の数が n より少なければ、
        if left < n:
            comb.append('(')
            self.backtracking(res, n, comb, left + 1, right)
            comb.pop()
            
        # 左括弧の数が右括弧より多ければ、
        # (右括弧の前に左括弧が確実に存在することを保証するための条件)
        if left > right:
            comb.append(')')
            self.backtracking(res, n, comb, left, right + 1)
            comb.pop()
            