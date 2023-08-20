import unittest
from linked_list import LinkedList, Node


class LinkedListTests(unittest.TestCase):
    def test_initialization_empty_list(self):
        linked_list = LinkedList()
        self.assertEqual(repr(linked_list), "")

    def test_initialization_with_nodes(self):
        nodes = [1, 2, 3, 4]
        linked_list = LinkedList(nodes)
        self.assertEqual(repr(linked_list), "1 -> 2 -> 3 -> 4")

    def test_add_first(self):
        linked_list = LinkedList([1, 2, 3, 4])
        node_0 = Node(0)
        linked_list.add_first(node_0)
        self.assertEqual(repr(linked_list), "0 -> 1 -> 2 -> 3 -> 4")

    def test_add_last(self):
        linked_list = LinkedList([1, 2, 3, 4])
        node_5 = Node(5)
        linked_list.add_last(node_5)
        self.assertEqual(repr(linked_list), "1 -> 2 -> 3 -> 4 -> 5")

    def test_add_after(self):
        linked_list = LinkedList([1, 2, 3, 4])
        node_2_5 = Node(2.5)
        linked_list.add_after(2, node_2_5)
        self.assertEqual(repr(linked_list), "1 -> 2 -> 2.5 -> 3 -> 4")

    def test_add_after_node_not_found(self):
        linked_list = LinkedList([1, 2, 3, 4])
        node_10 = Node(10)
        with self.assertRaises(Exception) as context:
            linked_list.add_after(10, node_10)
        self.assertEqual(str(context.exception), "Node with data 10")

    def test_add_after_empty_list(self):
        empty_list = LinkedList()
        node_1 = Node(1)
        with self.assertRaises(Exception) as context:
            empty_list.add_after(0, node_1)
        self.assertEqual(str(context.exception), "List is empty")


if __name__ == '__main__':
    unittest.main()
