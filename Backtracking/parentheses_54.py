class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        self.backtracking(res, n, [], 0, 0)
        return res
    
    def backtracking(self, res, n, comb, left, right):
        
        if len(comb) == 2 * n:
            res.append(''.join(comb))
            
        if left < n:
            comb.append('(')
            self.backtracking(res, n, comb, left + 1, right)
            comb.pop()
            
        if left > right:
            comb.append(')')
            self.backtracking(res, n, comb, left, right + 1)
            comb.pop()
            
        
        
        
    
    '''
    流れ
    n=1
    ["()"]
    
    n=2
    ["(())"]
    ["(())", "()()"]
    
    n=3
    ["((()))"]
    ["((()))","(()())"]
    ["((()))","(()())","(())()"]
    ["((()))","(()())","(())()","()(())"]
    ["((()))","(()())","(())()","()(())","()()()"]
    '''