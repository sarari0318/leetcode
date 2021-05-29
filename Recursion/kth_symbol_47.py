class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        if n == 1:
            return 0
        
        else:
            # kが偶数のとき
            if k % 2 == 0:
                # even index of current level is opposite of parent level's [(K+1)//2]
                return 0 if self.kthGrammar(n - 1, (k + 1) // 2) else 1
            # kが奇数のとき
            else:
                # odd index of current level is the same as parent level's [(K+1)//2]
                return 1 if self.kthGrammar(n - 1, (k + 1) // 2) else 0
            
        return int(res)