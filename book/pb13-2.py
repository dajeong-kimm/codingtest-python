# 팰린드롬 연결 리스트

# 연결 리스트가 팰린드롬 구조인지 판별하라

# 2. 데크를 이용한 최적화

from ast import List
import collections
from typing import Deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome (self, head: ListNode) -> bool:
    q: Deque = collections.deque()

    if not head:
        return True
    
    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) >1:
        if q.popleft() != q.pop():
            return False
    return True
    