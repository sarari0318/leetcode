class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.k = k
        self.nums = nums
        # self.numsをヒープ化
        heapq.heapify(self.nums)

        # self.numsの要素数がkより多い場合、
        # 要素数をkにする
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        # もしself.numsの要素数がself.kより少ない時、
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        # もしself.numsの根がvalより小さい時、
        elif self.nums[0] < val:
            heapq.heapreplace(self.nums, val)

        return self.nums[0]
