class Solution(object):
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    m, n, p = 0, 0, 0
    word = []

    def exist(self, board, word):
        self.word = word
        self.m = len(board)
        self.n = len(board[0])
        self.p = len(word)
        if self.p == 1:
            for i in range(self.m):
                for j in range(self.n):
                    if board[i][j] == word[0]:
                        return True
            return False

        visited = [[False for j in range(self.n)] for i in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:

                    visited[i][j] = True

                    if self.dfs(board, visited, 1, i, j) == True:

                        return True
                    visited[i][j] = False
        return False

    def dfs(self, board, visited, k, i, j):

        for dir in self.direction:
            if self.check(board, visited, k, i + dir[0], j + dir[1]):
                visited[i + dir[0]][j + dir[1]] = True
                if k == self.p - 1:
                    return True
                else:
                    k = k + 1
                if self.dfs(board, visited, k, i + dir[0], j + dir[1]) == True:
                    return True
                else:
                    visited[i + dir[0]][j + dir[1]] = False
                    k = k - 1
        return False

    def check(self, board, visited, k, i, j):

        if i < 0 or i == self.m:
            return False
        if j < 0 or j == self.n:
            return False
        if visited[i][j] == True:
            return False
        if board[i][j] != self.word[k]:
            return False
        return True


if __name__ == "__main__":
    test = Solution()
    print(test.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="T"))
