class MyStack(object):

    def __init__(self):
        self.list = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.list = [x] + self.list
        

    def pop(self):
        """
        :rtype: int
        """
        return self.list.pop(0)
        

    def top(self):
        """
        :rtype: int
        """
        return self.list[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not(self.list)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()