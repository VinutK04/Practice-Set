class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_lenght(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_lenght():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count +=1
        
    def inset_at(self, index, data):
        if index < 0 or index >= self.get_lenght():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_begining(data)

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def print(self):
        if self.head is None:
            print("Empty")
            return
        
        itr = self.head
        listr = ''
        while itr:
            listr += str(itr.data) + " ==> "
            itr = itr.next
        print(listr)

li = LinkedList()
# li.insert_at_begining(10)
# li.insert_at_end(20)
# li.insert_at_begining(30)
# li.insert_at_end(40)
li.insert_values(["Car", "Bike", "Aeroplane", "Rocket", "SpaceShip"])
li.print()
li.remove_at(0)
li.print()
li.inset_at(4, "Something")
li.print()
