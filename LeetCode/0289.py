class Solution:
    '''
    Traverse the board and examine every cell's neighbors. Change an element to 2 if it's currently 0 and will become 1; change an element to 3 if it's currently 1 and will become 0. 
    Time complexity: O(n), Space complexity: O(1) (considering only extra space created in the method).
    '''
    def gameOfLife(self, board: List[List[int]]) -> None:
        numR, numC = len(board), len(board[0])
        for r in range(numR):
            for c in range(numC):
                count = 0
                for dr, dc in [(0, 1), (1, 0), (1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1), (-1, 1)]:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= numR or nc < 0 or nc >= numC:
                        continue
                    if board[nr][nc] == 1 or board[nr][nc] == 3:
                        count += 1
                if count < 2:
                    if board[r][c] == 1:
                        board[r][c] = 3
                elif count > 3:
                    if board[r][c] == 1:
                        board[r][c] = 3
                elif count == 3:
                    if board[r][c] == 0:
                        board[r][c] = 2
        for r in range(numR):
            for c in range(numC):
                if board[r][c] == 2:
                    board[r][c] = 1
                elif board[r][c] == 3:
                    board[r][c] = 0
        return board