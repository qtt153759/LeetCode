from itertools import combinations


class Solution:
    def maximumRows(self, mat, cols):
        m, n = len(mat), len(mat[0])
        maxRows = 0

        colToChoose = list(combinations(list(range(n)), cols))
        print(colToChoose)
        for col in colToChoose:
            col = set(col)
            rowHidden = 0
            for row in mat:
                canHide = True
                for i in range(n):
                    if row[i] and i not in col:
                        canHide = False
                        break
                if canHide:
                    rowHidden += 1
            maxRows = max(maxRows, rowHidden)
        return maxRows


if __name__ == "__main__":
    test = Solution()
    print(test.maximumRows(mat=[[1], [0]], cols=1))
