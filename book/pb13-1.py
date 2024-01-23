# 팰린드롬 연결 리스트

# 연결 리스트가 팰린드롬 구조인지 판별하라

# 1. 리스트 변환

from ast import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome (self, head: ListNode) -> bool:
    q: List = []

    if not head:
        return True
    
    node = head

    while node is not None:
        q.append(node.val)
        node = node.next
    
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False
    
    return True