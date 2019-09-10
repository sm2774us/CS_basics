# Implement an iterator to flatten a 2d vector.

# For example,
# Given 2d vector =

# [
#   [1,2],
#   [3],
#   [4,5,6]
# ]
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,2,3,4,5,6].

# Hint:

# How many variables do you need to keep track?
# Two variables is all you need. Try with x and y.
# Beware of empty rows. It could be the first few rows.
# To write correct code, think about the invariant to maintain. What is it?
# The invariant is x and y must always point to a valid point in the 2d vector. Should you maintain your invariant ahead of time or right when you need it?
# Not sure? Think about how you would implement hasNext(). Which is more complex?
# Common logic in two different places should be refactored into a common method.

# V0 

# V1
# https://www.jiuzhang.com/solution/flatten-2d-vector/#tag-highlight-lang-python
class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.row, self.col, self.vec2d = 0, 0, vec2d
        

    # @return {int} a next element
    def next(self):
        # Write your code here
        self.col += 1
        return self.vec2d[self.row][self.col - 1]
        

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        while self.row < len(self.vec2d) and \
            self.col >= len(self.vec2d[self.row]):
            self.row, self.col = self.row + 1, 0
        return self.row < len(self.vec2d)

# V1'
# https://www.jiuzhang.com/solution/flatten-2d-vector/#tag-highlight-lang-python
class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        self.vec2d = vec2d
        self.row, self.col = 0, -1
        self.next_elem = None

    # @return {int} a next element
    def next(self):
        if self.next_elem is None:
            self.hasNext()
            
        temp, self.next_elem = self.next_elem, None
        return temp

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        if self.next_elem:
            return True
        
        self.col += 1
        while self.row < len(self.vec2d) and self.col >= len(self.vec2d[self.row]):
            self.row += 1
            self.col = 0
            
        if self.row < len(self.vec2d) and self.col < len(self.vec2d[self.row]):
            self.next_elem = self.vec2d[self.row][self.col]
            return True
            
        return False
        
# V1'' 
# http://www.voidcn.com/article/p-qxkyrjri-zo.html
class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec = vec2d
        self.row = 0
        self.col = 0
        i = 0
        while self.row != len(self.vec):
            if len(self.vec[self.row]) != 0:
                self.col = 0
                break
            self.row += 1

    def next(self):
        """
        :rtype: int
        """
        ret = self.vec[self.row][self.col]
        self.col += 1
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.row == len(self.vec):
            return False
        if self.col != len(self.vec[self.row]):
            return True
        else:
            self.row += 1
            while self.row != len(self.vec):
                if len(self.vec[self.row]) != 0:
                    self.col = 0
                    return True
                self.row += 1
            return False
# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())

# V2 
# Time:  O(1)
# Space: O(1)
from collections import deque
class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        #self.stack = deque((len(v), iter(v)) for v in vec2d if v)
        self.stack = deque((len(v), list(iter(v))) for v in vec2d if v) # fix for python 3 

    def next(self):
        """
        :rtype: int
        """
        length, iterator = self.stack.popleft()
        if length > 1:
            self.stack.appendleft((length-1, iterator))
        return next(iterator)

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.stack)