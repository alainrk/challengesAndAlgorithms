# This is an input class. Do not edit.
class LinkedList:
  def __init__(self, value):
    self.value = value
    self.next = None


def findLoop(head):
	slow, fast = head.next, head.next.next
	while slow != fast:
		slow, fast = slow.next, fast.next.next
	slow = head
	while slow != fast:
		slow, fast = slow.next, fast.next
	return slow
