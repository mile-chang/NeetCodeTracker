class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Solution 1: we can init 3 array(row, column, 3*3 sub-boxes) to store dights, then we determine those array is reptition or not.
        # time complextiy O(N2) or O(1)、space complextiy O(N2) or O(1), because the Constraints set always 9*9 sudoku.
        # init set hash 

        # Note: collections not collection, defaultdict not dict
        row = collections.defaultdict(set)
        column = collections.defaultdict(set)
        sub_box = collections.defaultdict(set)

        # Step 1: add cells in set hash (raw, column, sub_box)
        # determine is valid or not, when we increase value in the hash set
        for r in range(9):
            for c in range(9):
                cells = board[r][c]
                # Note: I need to check first, then update the value in hash set
                if cells != ".":
                    if (cells in row[r] or
                        cells in column[c] or
                        cells in sub_box[r // 3, c // 3]):
                        return False
                    row[r].add(cells)
                    column[c].add(cells)
                    sub_box[r // 3, c // 3].add(cells)
        return True

