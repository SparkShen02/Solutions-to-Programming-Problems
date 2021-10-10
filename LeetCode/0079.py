class Solution:
    # Run a depth first search for every position of the board that contains word[0]. 
    def exist(self, board: List[List[str]], word: str) -> bool:
        numRow = len(board)
        numCol = len(board[0])
        for r in range(numRow):
            for c in range(numCol):
                if board[r][c] != word[0]:
                    continue

                # DFS
                toVisit = [(0, [(r, c)], r, c)]
                while len(toVisit) != 0:
                    i, curPath, curR, curC = toVisit.pop()

                    # i indicates that current letter should match word[i]
                    if board[curR][curC] != word[i]: 
                        continue
                    if i == len(word) - 1:
                        return True

                    for rDiff, cDiff in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        newR = curR + rDiff
                        newC = curC + cDiff
                        if newR < 0 or newC < 0 or newR >= numRow or newC >= numCol:
                            continue
                        if (newR, newC) in curPath:
                            continue
                        toVisit.append([i + 1, curPath + [(newR, newC)], newR, newC])
        return False