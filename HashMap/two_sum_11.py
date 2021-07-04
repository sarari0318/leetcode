class Solution:
    def twoSum(self, nums, target):

        '''
        Parameters
        ----------
            nums: List[int]
            target: int
        Returns
        -------
            List[int]
            ⇨ return a list including the numbers' indexes which the total is target.
        '''

        # 要素とそのindexを記録
        hash_map = {}

        for idx, num in enumerate(nums):
            if target - num in hash_map.keys():
                return [hash_map[target - num], idx]

            # 各要素のindexをhash_mapに記録
            hash_map[num] = idx
            