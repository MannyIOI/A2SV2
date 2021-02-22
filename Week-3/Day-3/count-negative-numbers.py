class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        col = len(grid[0]) - 1
        # start from the bottom right of the matrix
        for row in range(len(grid) - 1, -1, -1):
            # binary search vertically and horizontally
            bottom = row
            top = 0
            pos = 0
            
            if col < 0:
                break
                
            if grid[row][col] >= 0:
                break
            
            # bottom to up search
            while top <= bottom:
                mid = top + (bottom - top) // 2
                if grid[mid][col] < 0:
                    pos = mid
                    bottom = mid - 1
                else:
                    top = mid + 1
            
            # bottom to up count
            count += row + 1 - pos
            
            right = col
            left = 0
            pos = 0
            
            # right to left search
            while left <= right:
                mid = left + (right - left) // 2
                if grid[row][mid] < 0:
                    pos = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            # right to left count
            count += col + 1 - pos
            # remove counting self twice
            count -= 1
            
            col = col - 1
            
        return count