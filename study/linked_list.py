class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)

class SingleLinkedList:
    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.list_size = 1

    def __str__(self):
        print_list = '['
        node = self.head
        while True:
            print_list += str(node)
            if node.next == None:
                break
            node = node.next
            print_list += ', '
        print_list += ' ]'
        return print_list

    def insertFirst(self, data):
        new_node = Node(data)
        temp_node = self.head
        self.head = new_node
        self.head.next = temp_node

        self.list_size +=1

    def selectNode(self, num):
        if self.list_size < num:
            return
        node = self.head
        count = 0
        while count < num:
            node = node.next
            count += 1
        return node
    
    def insertLast(self, data):
        node = self.head
        while True:
            if node.next == None:
                break
            node = node.next

        new_node = Node(data)
        node.next = new_node
        self.list_size += 1

    def insertMiddle(self, num, data):
        if self.head.next == None:
            insertLast(data)
            return
        node = self.selectNode(num)
        new_node = Node(data)
        temp_next = node.next
        node.next = new_node
        new_node.next = temp_next
        self.list_size += 1

    

    def selectNode(self, num):
        if self.list_size<num:
            return
        
        node=self.head
        count =0
        while count <num:
            node=node.next
            count+=1
        return node 

    def deleteNode(self, num):
        if self.list_size <1:
            return
        if self.list_size < num:
            return
        
        if num == 0:
            self.deleteHead()
            return
        node = self.selectNode(num-1)

        node.next = node.next.next
        del_node = node.next
        del del_node 

    def deleteHead(self):
        node = self.head
        self.head = node.next
        del node

    def size(self):
        return str(self.list_size)