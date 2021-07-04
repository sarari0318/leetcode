import collections

class Solution:
    def firstUniqChar(self, s):

        '''
        Parameters
        ----------
            s: str
        Returns
        -------
            int
            ⇨ return the first non-repeating character in it and return its index. 
            If it does not exist, return -1.
        '''
        
        # sに含まれる各スペルの数を記録するhashmap
        counter = collections.Counter(s)
        
        # 固有のスペルのindexを記録するリスト
        indexes = []
        for key, val in counter.items():
            if val == 1:
                indexes.append(s.index(key))
                
        return min(indexes) if indexes else -1