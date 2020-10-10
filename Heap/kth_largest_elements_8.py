class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

        heapq.heapify(self.nums)

        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)

        elif self.nums[0] < val:
            heapq.heapreplace(self.nums, val)

        return self.nums[0]

    # testcase1: k=3, nums[4, 5, 8, 2], val=3
    # nums[2, 4, 5, 8]
    # heapq.heappop(nums) ⇨ nums[4, 5, 8]
    # add(self.nums, 3) ⇨ nums[4, 5, 8]
    # return 4 ⇨ Accepted!!

    # testcase2: k=3, nums[4, 5, 8, 2], val=5
    # nums[2, 4, 5, 8]
    # heapq.heappop(nums) ⇨ nums[4, 5, 8]
    # add(self.nums, 5) ⇨ nums[5, 5, 8]
    # return 5 ⇨ Accepted!!