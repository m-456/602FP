# Robert Plastina
# 4-19-2024
# This contains the classes necessary for a Stack

class Node:
    def __init__(self, data, nextNode=None):
        self.__nodeData = data
        self.__nextNode = nextNode

    def getNodeData(self):
        return self.__nodeData

    def getNextNode(self):
        return self.__nextNode

    def setNodeData(self, nd):
        self.__nodeData = nd

    def setNextNode(self, nn):
        self.__nextNode = nn

class EmptyStackException(Exception):
    def __init__(self, action):
        self.error_message = f"{action} cannot be performed, Stack is empty"
        super().__init__(self.error_message)

class Stack:
    def __init__(self):
        self.__head = None
        self.__size = 0

    def isEmpty(self):
        return self.__head is None

    def push(self, data):
        newNode = Node(data, self.__head)
        self.__head = newNode
        self.__size += 1

    def pop(self):
        if self.isEmpty():
            raise EmptyStackException("pop")
        data = self.__head.getNodeData()
        self.__head = self.__head.getNextNode()
        self.__size -= 1
        return data

    def peek(self):
        if self.isEmpty():
            raise EmptyStackException("peek")
        return self.__head.getNodeData()

    def clear(self):
        self.__head = None
        self.__size = 0

    def size(self):
        return self.__size

    def __str__(self):
        if not self.__head:
            return ""
        current = self.__head
        stackList = []
        while True:
            stackList.append(str(current.getNodeData()))
            current = current.getNextNode()
            if current is None:
                break
        return ", ".join(stackList)
