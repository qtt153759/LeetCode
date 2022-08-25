import time


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printList(self):
        tmp = self
        while tmp != None:
            print("val", tmp.val)
            tmp = tmp.next


class Solution(object):
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        newHead = head.next
        tmp, first, second = ListNode(0, head), None, None
        while tmp.next != None and tmp.next.next != None:
            # shift
            first = tmp.next
            second = first.next
            # print(tmp.val, "<->", first.val, "<->", second.val)
            # swap
            first.next = second.next
            second.next = first
            tmp.next = second
            # print(tmp.val, "<->", first.val, "<->", second.val)
            tmp = first

            # print(tmp.val, "<->", first.val, "<->", second.val)
            # time.sleep(1)
        return newHead


if __name__ == "__main__":
    test = Solution()

    head = ListNode(1)
    tmp = head
    head.next = ListNode(2)
    head = head.next
    head.next = ListNode(3)
    head = head.next
    head.next = ListNode(4)
    tmp.printList()
    test.swapPairs(tmp).printList()
