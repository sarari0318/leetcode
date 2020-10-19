import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        if s is None or s == "":
            return -1
        
        counter = collections.Counter(s)
        
        indexes = []
        for key, val in counter.items():
            if val == 1:
                indexes.append(s.index(key))
                
        return min(indexes) if indexes else -1