with open('sample_input.txt', 'r') as f:
    data = f.read().splitlines()

layout = []
for line in data:
    new_line = []
    for num in line:
        new_line.append(int(num))
    
    layout.append(new_line)

layout[0][0] = 0 #risk of first cell is 0

class Solution:

    def minPathSum(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        T = [[0] * n for _ in range(m)]
        # First left top corner cost is same.
        T[0][0] = grid[0][0]

        # First row in T
        for first_row_idx in range(1, n):
            T[0][first_row_idx] = T[0][first_row_idx-1] + grid[0][first_row_idx]

        # First col in T
        for first_col_idx in range(1, m):
            T[first_col_idx][0] = T[first_col_idx-1][0] + grid[first_col_idx][0]
    
        for i in range(1, m):
            for j in range(1, n):
                T[i][j] = grid[i][j] + min(T[i-1][j],   # top
                                           T[i][j-1])   # left

        return T[-1][-1]

s = Solution()
print(s.minPathSum(layout))




