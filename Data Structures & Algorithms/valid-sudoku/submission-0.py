class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #to define box to box to box i would add three
        #flat_index = (row_number × width_of_each_row) + column_number  
        #box_number = (row_band × 3) + col_band
        #one hashset for column, one for row, and one for box
        column_set = [set() for _ in range(9)]
        row_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]

        #1 Get the value at that cell.
        #Skip it if it's empty (Sudoku boards often use . for empty cells — worth checking how this problem represents empty cells).
#Otherwise, check: is this value already in rows[row]? Already in cols[col]? Already in boxes[box_index]?
#If it's in any of those → duplicate found → return False immediately.
#If not a duplicate, add it to all three sets so future cells can check against it.
        rows = len(board) 
        for i in range(rows):
            cols = len(board[i])  
            for j in range(cols):
                curr=board[i][j]
                box_index = (i//3)*3 + (j//3)
                if curr ==".":
                    continue
                if curr in column_set[j] or curr in row_set[i] or curr in box_set[box_index]:
                    return False
                else:
                    column_set[j].add(curr)
                    row_set[i].add(curr)
                    box_set[box_index].add(curr)
        return True
        
        
