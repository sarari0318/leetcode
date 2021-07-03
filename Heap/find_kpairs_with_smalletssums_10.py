class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        '''
        Parameters
        ----------
            nums: List[int]
            k: int
        Returns
        -------
            List[int]
            ⇨ return the k paris with the smallest sums
        '''

        heap = []

        # cornercase: nums1 or nums2 is None
        if nums1 is None or nums2 is None:
            return None

        for n1 in nums1:
            for n2 in nums2:
                if len(heap) < k:
                    heapq.heappush(heap, (-n1 - n2, [n1, n2]))
                elif -n1 - n2 > heap[0][0]:
                    heapq.heapreplace(heap, (-n1 - n2, [n1, n2]))
                else:
                    break
                    
        # return k pairs
        return [heapq.heappop(heap)[1] for _ in range(k) if heap]
        