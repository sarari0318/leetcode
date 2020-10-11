class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        # return the k paris with the smallest sums
        # pre: 2 arrays, and k
        # post: the k pairs with the smallest sums ⇨ List[List[int]]
        
        # step1: make k paris and sort ⇨ heapq.heappush()
        heap = []
        
        for n1 in nums1:
            for n2 in nums2:
                if len(heap) < k:
                    heapq.heappush(heap, (-n1-n2, [n1, n2]))
        
                # step2: if -n1-n2 > heap[0][0] ⇨　replace
                elif -n1-n2 > heap[0][0]:
                    heapq.heapreplace(heap, (-n1-n2, [n1, n2]))
                # fix①
                else:
                    break
                    
        # return k pairs
        return [heapq.heappop(heap)[1] for _ in range(k) if heap]
        