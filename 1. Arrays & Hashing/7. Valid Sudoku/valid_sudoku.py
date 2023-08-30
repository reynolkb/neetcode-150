import collections
from typing import List


class Solution(object):
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # key is column index, value is set
        cols = collections.defaultdict(set)
        # key is row index, value is set
        rows = collections.defaultdict(set)
        """
        key = the indexes which make up the square

        [
        [0,0], [0,1], [0,2],
        [1,0], [1,1], [1,2],
        [2,0], [2,1], [2,2],
        ]
        """
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                # // is integer (floor) division
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
