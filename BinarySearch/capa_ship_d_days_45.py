class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        '''
        Params
        ==============
            weights: List[int]
            days: int
        Returns
        ==============
            min_pack: int
            ⇨ return the least weight capacity of the ship that will 
            result in all the packages on the conveyor belt being shipped within days days.
        '''
        
        # １日あたりの積載量の最小値を一番重い荷物の重さ
        #                  最大値を全ての荷物の重さの合計とする
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            # day_counter: 何日要するかを記録
            # cur_weight: １日ごとに重さを記録
            day_counter, cur_weight = 1, 0
            for w in weights:
                if cur_weight + w > mid:
                    day_counter += 1
                    cur_weight = 0
                cur_weight += w
            # もしdaysよりも日にちがかかったら
            if day_counter > days:
                left = mid + 1
            else:
                right = mid
                
        return int(left)