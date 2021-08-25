# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def nodeSwap(head):
	tmp = LinkedList(0)
	tmp.next = head
	prev = tmp
	while prev.next is not None and prev.next.next is not None:
		curr = prev.next
		post = prev.next.next

		curr.next = post.next
		post.next = curr
		prev.next = post

		prev = curr

	return tmp.next