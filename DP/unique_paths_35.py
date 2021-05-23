class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        if obstacleGrid[0][0] == 1:
            return 0
        
        height, width = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0 for _ in range(width)] for _ in range(height)]
        dp[0][0] = 1
        
        for row in range(1, height):
            if obstacleGrid[row][0] == 0:
                dp[row][0] = dp[row - 1][0]
            
        for col in range(1, width):
            if obstacleGrid[0][col] == 0:
                dp[0][col] = dp[0][col - 1]


        for row in range(1, height):
        	for col in range(1, width):
        		if obstacleGrid[row][col] == 0:
        			dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[-1][-1]