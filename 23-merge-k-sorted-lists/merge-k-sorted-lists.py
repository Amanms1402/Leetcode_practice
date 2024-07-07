class Solution:
    def mergeKLists(self, lists):
        # Base case: If there are no linked lists, return None
        if not lists:
            return None

        # Base case: If there is only one linked list, return it
        if len(lists) == 1:
            return lists[0]

        # Divide the lists into two halves
        mid = len(lists) // 2
        left = lists[:mid]
        right = lists[mid:]

        # Recursively merge the left and right halves
        merged_left = self.mergeKLists(left)
        merged_right = self.mergeKLists(right)

        # Merge the two merged halves
        return self.merge(merged_left, merged_right)

    def merge(self, l1, l2):
        # Base case: If either of the lists is empty, return the other list
        if not l1:
            return l2
        if not l2:
            return l1

        # Recursively merge the lists based on the smaller value
        if l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2