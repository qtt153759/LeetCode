class Solution(object):
    def isValidSudoku(self, board):
        big = set()
        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x == ".":
                    continue
                if (i, x) in big or (x, j) in big or (i // 3, j // 3, x) in big:
                    return False
                big.add((i, x))
                big.add((x, j))
                big.add((i // 3, j // 3, x))
        return True


if __name__ == "__main__":
    test = Solution()
    print(
        test.isValidSudoku(
            [
                ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ]
        )
    )
