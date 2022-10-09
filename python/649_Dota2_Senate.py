from queue import Queue


class Solution(object):
    def predictPartyVictory(self, senate):
        q1, q2 = Queue(), Queue()
        for i in range(len(senate)):
            if senate[i] == "Radiant":
                q1.put(senate[i])
            else:
                q2.put(senate[i])
        while q1.qsize() > 0 and q2.qsize() > 0:
            index_1, index_2 = q1.get(), q2.get()
            if index_1 < index_2:
                q1.put(index_1)
            else:
                q2.put(index_2)
        if q1.qsize() > q2.qsize():
            return "Radiant"
        return "Dire"


test = Solution()
print(test.predictPartyVictory("DDRRR"))
