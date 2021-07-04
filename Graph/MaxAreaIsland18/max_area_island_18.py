class Solution:
    def maxAreaOfIsland(self, grid):

        '''
        Parameters
        ----------
            grid: List[List[int]]
        Returns
        -------
            int
            ⇨ return the maximum area of an island in grid. If there is no island, return 0.
        '''
        
        ver, hor = len(grid), len(grid[0])
        
        def dfs(i, j):
            # gridの枠内で、かつgird[i][j]が 1(島)である時、
            if 0 <= i < ver and 0 <= j < hor and grid[i][j]:
                grid[i][j] = 0
                return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
            return 0
        
        count = [dfs(i, j) for i in range(ver) for j in range(hor) if grid[i][j]]
        return max(count) if count else 0