class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):

        '''
        Parameters
        ----------
            obstacleGrid: List[List[int]]
        Returns
        -------
            int
            ⇨ return the number of unique paths of obstacleGrid.
        '''
        
        # もしスタート地点が行き止まりだったら、
        if obstacleGrid[0][0] == 1:
            return 0
        
        height, width = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0 for _ in range(width)] for _ in range(height)]
        # スタート地点は行き止まりではないので、1を入れる
        dp[0][0] = 1
        
        for row in range(1, height):
            # もしobstacleGrid[row][0] が行き止まりでなければ、
            if obstacleGrid[row][0] == 0:
                dp[row][0] = dp[row - 1][0]
            
        for col in range(1, width):
            # もしobstacleGrid[0][col] が行き止まりでなければ、
            if obstacleGrid[0][col] == 0:
                dp[0][col] = dp[0][col - 1]


        for row in range(1, height):
        	for col in range(1, width):
                # もしobstacleGrid[row][col] が行き止まりでなければ、
        		if obstacleGrid[row][col] == 0:
        			dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[-1][-1]