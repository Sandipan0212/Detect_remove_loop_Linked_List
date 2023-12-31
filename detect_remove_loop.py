# -*- coding: utf-8 -*-
"""detect_remove_loop.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oaLBjASHJ2wwRq7H0hrsc6IkzZ_3_Iv4
"""

class Node:
  def __init__(self,data):
    self.data = data
    self.next = None


#input to linked list
def takeinputloop():
  inputlist = [int(x) for x in input().split()]
  head = None
  tail = None
  for i in inputlist:
    if i == -1:
      break
    newnode = Node(i)
    if head is None:
      head = newnode
      tail = newnode
    else:
      tail.next = newnode
      tail = newnode

  ptr = head
  ptr = ptr.next.next
  tail.next = ptr
  return head

#print linked list
def printL(a):
  while a is not None:
    print(str(a.data)+"->",end = " ")
    a = a.next
  print("None")
  #print("hello")
  return

def loop(head):
  slow = head
  fast = head
  while fast.next != None and fast.next.next != None:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      return slow
  return

def remove_loop(head):
  meet = loop(head)
  start = head
  prev = None
  while start != meet:
    prev = meet
    start = start.next
    meet = meet.next
  prev.next = None
  return head

a = takeinputloop()

b = remove_loop(a)
printL(b)



