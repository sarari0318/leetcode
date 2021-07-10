class Solution:
    def nextPermutation(self, nums):

        """

        Parameters
        ----------
            nums: List[int]
        Returns
        -------
            None
            ⇨ Do not return anything, modify nums in-place instead.
        """

        N = len(nums)
        pivot = 0

        # 大小が前から順になっているところを探す
        for i in range(N - 1, 0, -1):
            # 条件①
            if nums[i - 1] < nums[i]:
                pivot = i
                break

        # もし条件①に該当する箇所がなく、完全に降順に並んでいたら、
        if pivot == 0:
            # next permutationは昇順にソートされた状態
            nums.sort()
            return

        swap = N - 1
        while nums[pivot - 1] >= nums[swap]:
            swap -= 1

        nums[swap], nums[pivot - 1] = nums[pivot - 1], nums[swap]
        nums[pivot:] = sorted(nums[pivot:])