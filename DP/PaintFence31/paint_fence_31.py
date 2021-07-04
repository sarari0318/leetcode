'''
There is a fence with n posts, each post can be painted with one of the k colors.
You have to paint all the posts such that no more than two adjacent fence posts have the same color.
Return the total number of ways you can paint the fence.
Note:
n(柵の数) and k(色の数) are non-negative integers.
'''

class Solution:
    def numWays(self, n, k):

        '''
        Params:
            n: int
            k: int
        Returns:
            int
            return the total number of ways you can paint the fence.
        '''

        # 柵の数が0の時
        if n == 0:
            return 0

        elif n == 1:
            return k

        # 同じ色の柵が２つ並ぶ時
        # (k通りの色のパターン)×(１つ前と同じ色のパターン数)
        same = k * 1
         # 違う色が２つ並ぶ時
         # (k通りの色のパターン)×(１つ前とは異なる色のパターン数)
        diff = k * (k - 1)

        if n == 2:
            return same + diff

        # prev_same: 直近の２つに同じ色が続いている
        # prev_diff: 直近の２つに違う色が続いている
        prev_same, prev_diff = same, diff

        for i in range(3, n + 1):
            # 直前の色と同じにできるのは、直前の２つが異なる色である時
            # ここで選べる色のパターン数は、直前のフェンスの色と同じ色なので 1
            same = prev_diff * 1
            # 直前の色と異なる色を選ぶのは、直前の２つが同じ色 and 直前の２つが異なる色の時
            # ここで選べる色のパターン数は、直前のフェンスの色と異なる色なので k-1
            diff = (prev_same + prev_diff) * (k - 1)

            prev_same, prev_diff = same, diff

        return same + diff





