from pzt_rbt import RBTree, RBTreeNode

def test_node_create_and_show():
    print(RBTreeNode())
    print(RBTreeNode(0))

def test_tree_operation(insert_list, delete_list=[], show_type=-1, show_every_step=False):
    split_string = '----------------------------------------------------------'
    print(split_string)
    print(split_string)
    print('Inserting these node now: %s' % insert_list)
    tree = RBTree()
    for i in insert_list:
        tree.insert_node(RBTreeNode(i))
        if show_every_step:
            tree.show_tree(show_type)
            print(split_string)
    
    tree.show_tree(show_type)


    print('Deleting these node now: %s' % delete_list)
    for i in delete_list:
        del_node = tree.get_node(i)
        tree.delete_node(del_node)
        if show_every_step:
            tree.show_tree(show_type)
            print(split_string)
    tree.show_tree(show_type)
    print(split_string) 
    print(split_string)
    

if __name__ == '__main__':
    in_list = [1,2,3,4,5,6,7,8,9,10]
    #in_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    del_list = [4]
    test_tree_operation(in_list, del_list, show_every_step=False)
