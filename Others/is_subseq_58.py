class Solution:
    def isSubsequence(self, s, t):

        '''
        Parameters
        ----------
            s: str
            t: str
        Returns
        -------
            bool
            ⇨ return true if s is a subsequence of t, or false otherwise.
        '''

        # index_s: 文字列sのindex
        # index_t: 文字列tのindex
        index_s, index_t = 0, 0

        while index_s < len(s) and index_t < len(t):
            if s[index_s] == t[index_t]:
                index_s += 1
            index_t += 1

        # index_sがsの文字数分進んでいれば、True
        #                        いなければ、False
        return index_s == len(s)