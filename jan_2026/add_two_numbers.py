#https://leetcode.com/problems/add-two-numbers/submissions/1874070491/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_l,l2_l = [],[]
        
        self.list_constructor(l1,l1_l)
        self.list_constructor(l2,l2_l)
        
        l1_l.reverse()
        l2_l.reverse()
        
        n1 = self.get_number(l1_l)
        n2 = self.get_number(l2_l)
        sum_num = n1+n2
        
        sum_str_s =[i for i in str(sum_num)]
        sum_str_s.reverse()
        return_list = [int(i) for i in sum_str_s]

        r = self.link_list_constructor(return_list)

        return r
    
    def get_number(self,l:List[int]):
        # uses expanded form to make that number
        number = 0
        counter = 0
        for i in l:
            x = len(l)-1-counter
            number += i*(10**x)
            counter += 1
        return number
    
    def list_constructor(self,l:Optional[ListNode],return_list:list=[]):
        #link list into simple python list using recursion
        print(l.val)
        return_list.append(l.val)
        if l.next:
            self.list_constructor(l.next,return_list)
        else:
            return return_list
    
    def link_list_constructor(self,l):
        # converts python list to linked list
        head = ListNode(l[0])
        current_node = head
        for i in l[1:]:
            node = ListNode(i)
            current_node.next = node
            current_node = node
        return head

#Notes
#This was my first time learning linked lists
