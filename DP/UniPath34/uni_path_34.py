class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if not m or not n:
            return 0

        dp = [0] * n
        dp[0] = 1

        for _ in range(m):
            for col in range(1, n):
                dp[col] += dp[col-1]

        return dp[-1]

if __name__ == "__main__":
    solution = Solution()
    print(solution.uniquePaths(3, 7))