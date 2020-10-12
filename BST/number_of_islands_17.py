class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # return the number of islands
        # pre: grid
        # post: the number of islands
        
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
        if hor<0 or ver<0 or hor>=len(grid) or ver>= len(grid[0]) or grid[hor][ver]!='1':
            return
        
        grid[hor][ver] = '#'
        
        self.dfs(grid, hor+1, ver)
        self.dfs(grid, hor-1, ver)
        self.dfs(grid, hor, ver+1)
        self.dfs(grid, hor, ver-1)