# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 포인터 초기화
        slow, fast = head, head

        # fast와 fast.next가 None이 아닌 동안 반복
        while fast and fast.next:
            slow = slow.next       # 느리게 한 칸 이동
            fast = fast.next.next  # 빠르게 두 칸 이동

            if slow == fast:       # 두 포인터가 만나면 사이클 존재
                return True

        return False  # fast가 null에 도달하면 사이클이 없음  