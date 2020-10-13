class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Pre: strs
        # Post: List[List]
        
        # cornercase: strs is None
        if strs is None:
            return None
        
        # res, dict = [], {}
        
        # step1: linear scan from left to right of strs
        # & group same chars
        
#         for word in strs:
#             anag = "".join(sorted(word))
#             if anag not in dict:
#                 dict[anag] = [word]
#             else:
#                 dict[anag].append(word)
            
#         for anags in dict.values():
#             res.append(anags)
            
#         return res

        # solution2 
        dict = collections.defaultdict(list)
    
        for word in strs:
            sort = "".join(sorted(word))
            dict[sort].append(word)
            
        return dict.values()