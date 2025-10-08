class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        ans = []
        for _ in range(n-2):
            ans.append([0]*(n-2))
        for i in range(n-2):
            for j in range(n-2):
                windowMax = -1
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        if windowMax < grid[r][c]:
                            windowMax = grid[r][c]
                ans[i][j] = windowMax 
        return ans




