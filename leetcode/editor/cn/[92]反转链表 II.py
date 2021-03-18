# 给你单链表的头节点 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链
# 表节点，返回 反转后的链表 。
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点数目为 n 
#  1 <= n <= 500 
#  -500 <= Node.val <= 500 
#  1 <= left <= right <= n 
#  
# 
#  
# 
#  进阶： 你可以使用一趟扫描完成反转吗？ 
#  Related Topics 链表 
#  👍 772 👎 0
# from Cython.Compiler.ExprNodes import ListNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if head == None or head.next == None or left >= right or left < 0 or right < 0:
            return head

        h = ListNode(-1)
        h.next = head
        pre = h
        cur = head
        i = 1
        while i < left and cur != None:
            pre = cur
            cur = cur.next
            i += 1

        t1 = pre
        t2 = cur

        while i <= right and cur != None:
            lat = cur.next
            cur.next = pre
            pre = cur
            cur = lat
            i += 1

        t1.next = pre
        t2.next = cur
        return h.next

