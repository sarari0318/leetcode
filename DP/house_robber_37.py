class Solution:
    def rob(self, nums):

        '''
        Parameters
        ----------
            nums: List[int]
        Returns
        -------
            int
            ⇨ return the maximum amount of money you can rob tonight without alerting the police.
        '''
        
        house_num = len(nums)
        
        if house_num == 1:
            return nums[0]
        if house_num <= 3:
            return max(nums)
        
        # 住宅街がサークル状なので、
        # １軒目に入るか否かで２パターンに分ける
        # ① １軒目から盗む
        # ② 最後の家から盗む
        dp_1st, dp_last = [0 for _ in range(house_num)], [0 for _ in range(house_num)]
        
        dp_1st[0], dp_1st[1] = nums[0], nums[0]
        dp_last[0], dp_last[1] = 0, nums[1]
        
        for i in range(2, house_num - 1):
            dp_1st[i] = max(dp_1st[i - 2] + nums[i], dp_1st[i - 1])
        dp_1st[-1] = dp_1st[-2]
            
        for j in range(2, house_num):
            dp_last[j] = max(dp_last[j - 2] + nums[j], dp_last[j - 1])
            
        return max(dp_1st[-1], dp_last[-1])