class Solution:
    def intersection(self, nums1, nums2):

        '''
        Parameters
        ----------
            nums1: List[int]
            nums2: List[int]
        Returns
        -------
            List[int]
            ⇨ return an array of their intersection.
        '''
        
        res = []
        # それぞれのリストの要素を固有のものとするためにset型に変換
        uni_nums1, uni_nums2 = set(nums1), set(nums2)
        
        for n1 in uni_nums1:
            if n1 in uni_nums2:
                res.append(n1)
        
        return res
