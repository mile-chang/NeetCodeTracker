from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use hash sets to track seen numbers in rows, columns, and squares
        # Defaultdict is used to avoid key does not exist errors
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num != ".":
                    continue
                # Check if the number has already been seen in the current row, column, or square
                if (num in rows[r] or
                    num in cols[c] or
                    num in squares[(r // 3, c // 3)]):
                    return False
                # Update the sets with the current number
                rows[r].add(num)
                cols[c].add(num)
                squares[(r // 3, c // 3)].add(num)
        return True
