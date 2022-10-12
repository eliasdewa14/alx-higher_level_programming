#!/usr/bin/python3

"""Define a class Square."""


class Node:
    """Represent a square."""

    def __init__(self, data, next_node=None):
        """Initialize a new square.

        Args:
            data (int): The data of the new node
            next_node (Node): The next node of the new node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the node"""
        return self.__data

    @data.setter
    def data(self, value):
        if (type(value) != int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if (type(value) != Node and value):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    "Represent a singly linked list"

    def __init__(self):
        """Initialize a new singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node to the list.

        The node is inserted into list in numerical order

        Args:
            value (Node): The new node to insert into the list
        """
        new_node = Node(value)
        if (self.__head is None):
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            aux_node = self.__head
            while (aux_node):
                aux_node = aux_node.next_node
            new_node.next_node = aux_node.next_node
            aux_node.next_node = new_node

        def __str__(self):
            """Define the print function representation"""
            list = ""
            aux_node = self.__head
            while (aux_node):
                list += str(tmp_node.data)
                aux_node = aux_node.next_node
            return list
