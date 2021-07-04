class Solution:
    def wordBreak(self, s, wordDict):

        '''
        Parameters
        ----------
            s: str
            wordDict: List[str]
        Returns
        -------
            bool
            ⇨ return true if s can be segmented into a space-separated sequence of one or more dictionary words.
        '''

        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True

        return dp[-1]
