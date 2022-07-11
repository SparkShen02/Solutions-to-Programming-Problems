class Solution:
    '''
    Create a 9x9 list row, where row[r][n] = # of occurrances of digit n+1 in row r. 
    Create a 9x9 list col, where col[c][n] = # of occurrances of digit n+1 in column c. 
    Create a 3x3x9 list box, where box[rr][cc][n] = # of occurrances of digit n+1 in sub-box (rr, cc). 
    Traverse the board once. If # of occurrances of any digit in a row, column, or sub-box > 1, then the board is invalid. 
    Time complexity: O(1), Space complexity: O(1). 
    '''
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[0] * 9 for _ in range(9)]
        col = [[0] * 9 for _ in range(9)]
        sub = [[[0] * 9 for _ in range(3)] for _ in range(3)]
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                digit = int(board[r][c]) - 1
                row[r][digit] += 1
                col[c][digit] += 1
                sub[r//3][c//3][digit] += 1
                if row[r][digit] > 1 or col[c][digit] > 1 or sub[r//3][c//3][digit] > 1:
                    return False
        return True