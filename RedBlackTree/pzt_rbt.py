class RBTree(object):
    def __init__(self):
        self.nil = RBTreeNode()
        self.root = self.nil

class RBTreeNode(object):
    def __init__(self, key=None, value=None):
        self._key = key
        if not self.isNilNode():
            self._value = value
        self._parent = None
        self._left = None
        self._right = None
        self._red = False

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value
    
    @property
    def parent(self):
        return self._parent

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    def isRed():
        return self._red

    def set_parent(self, node):
        if self.isNilNode():
            print("Nil Node can not set parent")
        else:
            self._parent = node

    def set_left(self, node):
        if self.isNilNode():
            print("Nil Node can not set left")
        else:
            self._left = node

    def set_right(self, node):
        if self.isNilNode():
            print("Nil Node can not set right")
        else:
            self._right = node

    def set_color(self, isRed):
        if self.isNilNode():
            print("Nil Node can not set color")
        else:
            self._red = isRed

    def set_value(self, value):
        if self.isNilNode():
            print("Nil Node can not set value")
        else:
            self._value = value

    def isNilNode(self):
        return self.key == None

if __name__ == '__main__':
    nil = RBTreeNode()
    nil.set_parent(nil)
    node = RBTreeNode(1)
    node.set_parent(nil)
