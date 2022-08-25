class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True


if __name__ == "__main__":
    test = Solution()
    print(test.canConstruct("aa", "aab"))
