# 팰린드롬 연결 리스트

# 연결 리스트가 팰린드롬 구조인지 판별하라

# 4. 런너를 이용한 우아한 풀이

from ast import List
import collections
from typing import Deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(self, head: ListNode) -> bool:
    rev = None
    slow = fast = head

    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    
    
    if fast:
        slow=slow.next

    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    
    return not rev