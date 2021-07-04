class RBTree(object):
    def __init__(self):
        self.nil = RBTreeNode()
        self.root = self.nil

    def insertNode(self, node):
        point_a = self.nil
        point_b = self.root
        while point_b != self.nil:
            point_a = point_b
            if node.key < point_b.key:
                point_b = point_b.left
            elif node.key > point_b.key:
                point_b = point_b.right
            else:
                point_b.set_value(node.value)
                return point_b
        
        if point_a == self.nil:
            self.root = node
        elif node.key < point_a.key:
            point_a.set_left(node)
        else:
            point_a.set_right(node)
        node.set_parent(point_a)
        node.set_left(self.nil)
        node.set_right(self.nil)
        node.set_color(True)
        self.insertFixUp(node)
        
        return node

    def insertFixUp(self, node):
        if node == self.root:
            node.set_color(False)
            return
        parent = node.parent
        grandpa = parent.parent
        grandpa_left = grandpa.left
        grandpa_right = grandpa.right
        if not parent.isRed():
            return
        else:
            if grandpa_left.isRed() and grandpa_right.isRed():
                grandpa_left.set_color(False)
                grandpa_right.set_color(False)
                grandpa.set_color(True)
                self.insertFixUp(grandpa)
            else:
                if parent.is_parent_left():
                    if node.is_parent_right():
                        self.left_rotate(parent)
                        parent = grandpa.left
                    parent.set_color(False)
                    grandpa.set_color(True)
                    self.right_rotate(grandpa)
                elif parent.is_parent_right():
                    if node.is_parent_left():
                        self.right_rotate(parent)
                        parent = grandpa.right
                    parent.set_color(False)
                    grandpa.set_color(True)
                    self.left_rotate(grandpa)
                else:
                    self.not_child_of_parent()
                
    def not_child_of_parent(self):
        raise Exception("This node is not the child of its parent. Please check it!")

    def left_rotate(self, node):
        if node == self.nil or node.right == self.nil:
            return
        parent = node.parent
        right = node.right
        right_left = right.left

        if node.is_parent_left():
            parent.set_left(right)
        elif node.is_parent_right():
            parent.set_right(right)
        
        node.set_parent(right)
        node.set_right(right_left)

        right.set_parent(parent)
        right.set_left(node)

        right_left.set_parent(node)

        if node == self.root:
            self.root = right

    def right_rotate(self, node):
        if node == self.nil or node.left == self.nil:
            return
        parent = node.parent
        left = node.left
        left_right = left.right

        if node.is_parent_left():
            parent.set_left(left)
        elif node.is_parent_right():
            parent.set_right(left)

        node.set_parent(left)
        node.set_left(left_right)
        
        left.set_parent(parent)
        left.set_right(node)

        left_right.set_parent(node)

        if node == self.root:
            self.root = left
                        

    def show_tree(self, show_type=0):
        def show_mid(node):
            if node == self.nil:
                return
            show_mid(node.left)
            print(node)
            show_mid(node.right)

        def show_pre(node):
            if node == self.nil:
                return
            print(node)
            show_pre(node.left)
            show_pre(node.right)
                
        def show_post(node):
            if node == self.nil:
                return
            show_post(node.left)
            show_post(node.right)
            print(node)

        if show_type < 0:
            show_pre(self.root)
        elif show_type > 0:
            show_post(self.root)
        else:
            show_mid(self.root)

    def get_tree_depth(self):
        def get_node_depth(node):
            if node == self.nil:
                return 0
            right_depth = get_node_depth(node.right)
            left_depth = get_node_depth(node.left)
            return left_depth + 1 if left_depth > right_depth else right_depth + 1
        return get_node_depth(self.root)

class RBTreeNode(object):
    def __init__(self, key=None, value=None):
        self._key = key
        if not self.is_nil_node():
            self._value = value
        else:
            self._value = None
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

    def isRed(self):
        return self._red

    def set_parent(self, node):
        if self.is_nil_node():
            print("Nil Node can not set parent")
        else:
            self._parent = node

    def set_left(self, node):
        if self.is_nil_node():
            print("Nil Node can not set left")
        else:
            self._left = node

    def set_right(self, node):
        if self.is_nil_node():
            print("Nil Node can not set right")
        else:
            self._right = node

    def set_color(self, isRed):
        if self.is_nil_node():
            print("Nil Node can not set color")
        else:
            self._red = isRed

    def set_value(self, value):
        if self.is_nil_node():
            print("Nil Node can not set value")
        else:
            self._value = value

    def is_nil_node(self):
        return self.key == None

    def is_parent_left(self):
        if self.is_nil_node():
            return False
        parent = self.parent
        if parent is None or parent.is_nil_node():
            return False
        else:
            return self == parent.left

    def is_parent_right(self):
        if self.is_nil_node():
            return False
        parent = self.parent
        if parent is None or parent.is_nil_node():
            return False
        else:
            return self == parent.right

    def __del__(self):
        if not self.is_nil_node():
            print("Deleting %s Node" % self.key)
            self.set_value(None)
            self.set_parent(None)
            self.set_left(None)
            self.set_right(None)
            self.set_color(False)

    def __repr__(self):
        node_info = "Key: %s, Value: %s, Color: %s, Parent: %s %s;"
        color = 'RED' if self.isRed() else 'BLACK'
        parent_key = self.parent.key if self.parent is not None else 'No Parent' 
        parent_relationship = None
        if self.is_parent_left():
            parent_relationship = 'LEFT'
        elif self.is_parent_right():
            parent_relationship = 'RIGHT'
        if self.is_nil_node():
            return node_info % (self.key, self.value, color, None, None)
        else:
            return node_info % (self.key, self.value, color, parent_key, parent_relationship)

