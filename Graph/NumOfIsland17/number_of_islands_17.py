class Solution:
    def numIslands(self, grid):

        '''
        Parameters
        ----------
            grid: List[List[str]]
        Returns
        -------
            int
            ⇨ return the number of islands
        '''
        
        if not grid:
            return 0
        
        count = 0
        
        for hor in range(len(grid)):
            for ver in range(len(grid[0])):
                if grid[hor][ver] == '1':
                    count += 1
                    self.dfs(grid, hor, ver)
                    
        return count
                
    def dfs(self, grid, hor, ver):
        # 枠外、もしくはgrid[hor][ver]が'1'の時、
        if hor < 0 or ver < 0 or hor >= len(grid) or ver >= len(grid[0]) or grid[hor][ver] != '1':
            return
        
        grid[hor][ver] = '#'
        
        # 下へ
        self.dfs(grid, hor + 1, ver)
        # 上へ
        self.dfs(grid, hor - 1, ver)
        # 右へ
        self.dfs(grid, hor, ver + 1)
        # 左へ
        self.dfs(grid, hor, ver - 1)