class RBTree(object):
    def __init__(self):
        self.nil = RBTreeNode()
        self.root = self.nil

    def insert_node(self, node):
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

        self.insert_fix_up(node)
        
        return node

    def insert_fix_up(self, node):
        if node == self.root:
            node.set_color(False)
            return
        parent = node.parent
        grandpa = parent.parent
        grandpa_left = grandpa.left
        grandpa_right = grandpa.right
        if not parent.is_red():
            return
        else:
            if grandpa_left.is_red() and grandpa_right.is_red():
                grandpa_left.set_color(False)
                grandpa_right.set_color(False)
                grandpa.set_color(True)
                self.insert_fix_up(grandpa)
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
                
    def node_is_not_parent_child(node):
        print('Node %s is not its parent %s child' %(node.key, node.parent.key))

    def delete_node(self, node):
        if node == self.nil:
            return

        if node == self.root:
            self.root = node

        if node.left.is_nil_node() and node.right.is_nil_node():
            
            #FixUp
            #DeleteNode
            if node.is_parent_left():
                node.parent.set_left(self.nil)
            elif node.is_parent_right():
                node.parent.set_right(self.nil)
            else:
                self.node_is_not_parent_child(node)
            del node
        elif node.left.is_nil_node() and not node.right.is_nil_node():
            #FixUp
            if node.is_parent_left():
                node.parent.set_left(node.right) 
            elif node.is_parent_right():
                node.parent.set_right(node.right)
            else:
                self.node_is_not_parent_child(node)
            node.right.set_parent(node.parent)
            del node
        elif node.right.is_nil_node() and not node.left.is_nil_node():
            if node.is_parent_left():
                node.parent.set_left(node.left)
            elif node.is_parent_right():
                node.parent.set_right(node.left)
            else:
                self.node_is_not_parent_child(node)
            node.left.set_parent(node.parent)
            del node
        else:
            sub_node = node.right
            sub_node_left = sub_node.left
            while sub_node_left != self.nil:
                sub_node = sub_node.left
                sub_node_left = sub_node.left

            #FixUp

            sub_node_right = sub_node.right
            sub_node_parent = sub_node.parent
            if sub_node.is_parent_left():
                sub_node_parent.set_left(sub_node_right)
            elif sub_node.is_parent_right():
                sub_node_parent.set_right(sub_node.right)
            else:
                self.node_is_not_parent_child(sub_node)
            sub_node_right.set_parent(sub_node_parent)
            
            node_parent = node.parent
            node_left = node.left
            node_right = node.right
            if node.is_parent_left():
                node_parent.set_left(sub_node)
            elif node.is_parent_right():
                node_parent.set_right(sub_node)
            else:
                self.node_is_not_parent_child(node)
            sub_node.set_parent(node_parent)
            sub_node.set_left(node_left)
            sub_node.set_right(node_right)
            node_left.set_parent(sub_node)
            node_right.set_parent(sub_node)
            sub_node.set_color(node.is_red())
            del node

    def get_node(self, key):
        point = self.root
        while point != self.nil:
            if key < point.key:
                point = point.left
            elif key > point.key:
                point = point.right
            else:
                break 
        return point

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
        print('Tree depth: %s' % self.get_tree_depth())

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

    def is_red(self):
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

    def set_color(self, is_red):
        if self.is_nil_node():
            print("Nil Node can not set color")
        else:
            self._red = is_red

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
        color = 'RED' if self.is_red() else 'BLACK'
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

