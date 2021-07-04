import collections

class Solution:
    def groupAnagrams(self, strs):
        
        '''
        Parameters
        ----------
            strs: List[str]
        Returns
        -------
            List[List[str]]
            ⇨ return list group the anagrams together.
        '''
        
        # 同じスペルの単語をまとめるhashmap
        same_spells = collections.defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            same_spells[sorted_word].append(word)

        return [val for val in same_spells.values()]