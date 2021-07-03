class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        '''
        Parameters
        ----------
            nums: List[int]
            k: int
        Returns
        -------
            List[int]
            ⇨ return k numbers of the most frequent elements
        
        '''

        # 各要素とその数を記録
        counter = collections.Counter(nums)

        for num, count in counter.items():
            # countの多い順に並べたいが、heapは値が小さい順に並べるので、
            # -countをタプルの１つ目の要素とし、要素数の多い順に並べる
            heapq.heappush(num_counter, (-count, num))

        return [heapq.heappop(num_counter)[1] for _ in range(k)]