class Solution:
    def intersection(self, nums1, nums2):
        
        if nums1 is None or nums2 is None:
            return []
        
        res = []
        uni_nums1, uni_nums2 = set(nums1), set(nums2)
        
        for n1 in uni_nums1:
            if n1 in uni_nums2:
                res.append(n1)
        
        return res
