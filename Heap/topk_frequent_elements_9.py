class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # cornercase: this array is non-empyt, so don't have to think about this case
        
        # return k numbers of the most frequent elements
        # pre: nums, k
        # post: the k most frequent elements
        
        # counter, count_heap = {}, []
        # step1: count the number of each element
        # for num in nums:
        #     if num not in counter.keys():
        #         counter[num] = 1
        #     else:
        #         counter[num] += 1
        # ⇨ sumarize
        
        counter = collections.Counter(nums)
        count_heap = []
        
        for key, val in counter.items():
            count_heap.append((-val, key))
            
        heapq.heapify(count_heap)
        
        # step2: return the res array including the elements
        return [heapq.heappop(count_heap)[1] for _ in range(k) if count_heap]