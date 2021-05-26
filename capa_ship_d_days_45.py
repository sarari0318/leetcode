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
            
        最小の容量を見つける
        
        １日当たりの積載量として考えられる範囲は、
            最小値：weightsの中で最も重い荷物の重量
            最大値：全ての重さの合計
        ⇨ この中から、daysの日数で全ての荷物を運び終えるのに必要な
          最軽積載量を求める！
          
        ⇨ 小さい値から大きい値へと順に並んでおり、
          最小値を求める問題
        ⇨ Binary-Search使えるんじゃね！？
        ⇨ 試してみる！
        '''
        
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