"""
 An iterator to flatten a nested list of integers.

    Approach:
        We use a stack of iterators to traverse the nested list lazily.
        At each step, we fetch the next element from the top iterator.
        If it is an integer, we store it for `next()` to return.
        If it is a nested list, we convert it into an iterator and push it onto the stack.
        This allows us to traverse arbitrarily nested lists without flattening the entire structure upfront.

    Methods:
        - next(): Returns the next integer in the flattened order.
        - hasNext(): Returns True if there are more integers to traverse, False otherwise.

    Time Complexity:
        - Average O(1) per `next()` and `hasNext()` call (amortized over all elements).
        - Each element is processed exactly once.

    Space Complexity:
        - O(d), where d is the maximum depth of nesting, due to the iterator stack.

    The problem ran successfully on Leetcode.
"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.st = [iter(nestedList)]
        self.nextEl = 0

    def next(self) -> int:
        return self.nextEl.getInteger()

    def hasNext(self) -> bool:
        while self.st:
            self.nextEl = next(self.st[-1], None)
            if self.nextEl is None:
                self.st.pop()
            else:
                if self.nextEl.isInteger():
                    return True
                else:
                    self.st.append(iter(self.nextEl.getList()))
        return False

         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())