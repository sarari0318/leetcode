class Solution:
    def subarraySum(self, nums, k):
        
        count, total = 0, 0
        sumdict = {0:1}
        
        for num in nums:
            total += num
            
            if total-k in sumdict.keys():
                count += sumdict[total-k]
                
            if total in sumdict.keys():
                sumdict[total] += 1
            else:
                sumdict[total] = 1
            
        return count