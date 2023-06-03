"""In real world - use collections package from std"""


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

    def __repr__(self):
        return self.value


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(value=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(value=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.value))
            node = node.next
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return

        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_value, new_node):
        if self.head is None:
            raise Exception("List is empty")
        for node in self:
            if node.value == target_node_value:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception(f"Node with data {target_node_value}")


if __name__ == "__main__":
    llist = LinkedList(["a", "b", "c", "d", "e"])
    print(llist)

    llist.add_first(Node("0"))
    print(llist)

    llist.add_last(Node("f"))
    print(llist)

    llist.add_after("c", Node("cc"))
    print(llist)
