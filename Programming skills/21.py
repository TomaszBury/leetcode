# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(list1: list[int], list2: list[int]) -> list[int]:
        return_list:list[int] = (list1 + list2)
        return_list.sort()
        return return_list
    
list1 = [1,2,4]; list2 = [1,3,4]
assert Solution.mergeTwoLists(list1, list2) == [1,1,2,3,4,4]

list1 = []; list2 = []
assert Solution.mergeTwoLists(list1, list2) == []

list1 = []; list2 = [0]
assert Solution.mergeTwoLists(list1, list2) == [0]