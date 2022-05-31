class node:                    # to initialize node object
    def__init__(self, data):
    self.data = data
    self.next = None
class linkedlist:              # to initialize head to node
    def__init__(self):
    self.head = None
    def push(self, new_data):
        new_node = node(new_data)
        new_node.next = self.head
        self.head = new_node
    def middle(self, new_data, previous_node):
        if previous_node is None:
            return
        new_node = node(new_data)
        new_node.next = previous_node.next
        previous_node.next = new_node
    def last(self, new_data):
        new_node = node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while(last.next):
            last = last.next # traverse till, the last node
            last.next = new_node
    def delete(self, value):
        temp = self.head                  #  temp holds the value if the value  and
        if(temp.head is not None):        # temp is not none list is there
            if(temp.data==value):         #  then the value  we hold is to be deleted
                self.head = temp.next     # the value after temp is going to be head pointer will move to the
                temp = None               # and make temp free

    while(temp is not None):             # selecting the value to be deleted
        if temp.data = key:              # the first element then break
            break
        prev = temp                      # present  temp value store  as previous
        temp = temp.next                 # and value next to temp as temp

    if(temp==None):
        return
    prev.next = temp.next                # connecting the value prev.next to the value next to temporary value
    temp = None                          # and make temp free


    def  printlist(self):
        temp = self.head
        while(temp):
            print(temp.data,end="")  # we need to print data of node
            temp = temp.next

        # Deleting a node
    # def deleteNode(self, position):
    #
    #         if self.head is None:
    #             return
    #
    #         temp = self.head
    #
    #         if position == 0:
    #             self.head = temp.next
    #             temp = None
    #             return
    #
    #         # Find the key to be deleted
    #         for i in range(position - 1):
    #             temp = temp.next
    #             if temp is None:
    #                 break
    #
    #         # If the key is not present
    #         if temp is None:
    #             return
    #
    #         if temp.next is None:
    #             return
    #
    #         next = temp.next.next
    #
    #         temp.next = None
    #
    #         temp.next = next

if__name__ == '__main__':
    list = linkedlist()
    list.head = node(1)
    second = node(2)
    third = node(3)

    list.head.next = second;
    second.next = third;

    list.push(6);
    list.middle(list.head.next, 5);
    list.last(3);

    list.printlist()



    # # Search an element
    # def search(self, key):
    #
    #     current = self.head
    #
    #     while current is not None:
    #         if current.data == key:
    #             return True
    #
    #         current = current.next
    #
    #     return False

    # # Sort the linked list
    # def sortLinkedList(self, head):
    #     current = head
    #     index = Node(None)
    #
    #     if head is None:
    #         return
    #     else:
    #         while current is not None:
    #             # index points to the node next to current
    #             index = current.next
    #
    #             while index is not None:
    #                 if current.data > index.data:
    #                     current.data, index.data = index.data, current.data
    #
    #                 index = index.next
    #             current = current.next


class node:
    def__init__(self, data):
    self.data = data
    self.next = None


class linkedlist:
    def__init__(self):
    self.head = None


def push(self, new_data):
    new_node = node(new_data)
    new_node.next = self.head
    self.head = new_node


def middle(self, previous_node, new_data):
    new_node = node(new_data)
    new_node.next = previous_node.next
    previous_node.next = new_node


def last(self, new_data):
    new_node = node(new_data)
    if self.head is None:
        self.head = new_node
        return
    last = self.head
    while (last.next):
        last = last.next
        last.next = new_node


def delete(self, node_delete):
    temp = self.head
    if (temp.head is not None):
        if (temp.data == node_delete):
            self.head = temp.next
            temp = None


while (temp is not None):
    if temp.data = node_delete:
        break
    prev = temp
    temp = temp.next

if (temp == None):
    return
prev.next = temp.next
temp = None


def print(slef):
    temp = slef.head
    while (temp):
        print(temp.data, end="")
        temp = temp.next
