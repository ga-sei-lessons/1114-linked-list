# node clase, a single entry into our list
class Node:
    def __init__(self, data, next):
        self.data = data # value at this node
        self.next = next # next node in line (or -- None if this is the last node)
    
    def __str__(self):
        return f'{self.data}'

# node testing zone
# head = Node(1, None)
# # print(head)
# taco = Node(2, None)
# head.next = taco
# # print(head, head.next)
# third_node = Node(3, None)
# head.next.next = third_node
# print(head, head.next, head.next.next, head.next.next.next)

# manager class which holds all the methods and data for our lists
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0 # how many nodes are in the list

    # lets linkedlists work with python's len() method
    def __len__(self):
        return self.size

    def __str__(self):
        # if the list is empty, return immediately
        if len(self) == 0:
            return '[]'

        return_str = str(self.head)
        # keep a reference to the node currently being iterated
        current_node = self.head
        while current_node:
            # do logic with the nodes
            return_str += f' -> {current_node.next}'
            # advance the loop
            current_node = current_node.next
        
        return f'[ {return_str} ]'

    def insert_front(self, data):
        # create a new node at the front of the list, replacing the head
        new_node = Node(data, None)
        # if this is the first node, set both head and tail to be the new node
        if len(self) == 0:
            self.head = new_node
            self.tail = new_node
        # otherwise, set the new node's next to be the current head
        else:
            # set the new node's next to be the head
            new_node.next = self.head
            # replace the current head with the new node
            self.head = new_node
    
        # increment the list's size
        self.size += 1
    
    def insert_end(self, data):
        # create a new node
        new_node = Node(data, None)
        if len(self) == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # set new node to be the next of the current tail
            self.tail.next = new_node
            # replace tail with new node
            self.tail = new_node
        
        self.size += 1
        
    
    def insert_after(self, data, search):
        # iterate until we find the search value
        current_node = self.head
        while current_node:
            # compare values
            if current_node.data == search:
                # if we have a match, insert
                # new node's next needs to be current node's next
                new_node = Node(data, current_node.next)
                # overwrite current node's next with the new node
                current_node.next = new_node
                return
            
            current_node = current_node.next
        
        # if we are down here, no match was made, so just insert at the end
        self.insert_end(data)
        

my_list = LinkedList()
print('list should be empty:', my_list)
my_list.insert_front(1)
my_list.insert_front(2)
my_list.insert_front(3)
my_list.insert_end(10)
print("list len:", len(my_list))
print(my_list)
# print(my_list.head, my_list.head.next, my_list.head.next.next, my_list.head.next.next.next)

other_list = LinkedList()
other_list.insert_end(10)
other_list.insert_front(11)
other_list.insert_end(9)
other_list.insert_after(9.5, 10)
other_list.insert_after(7, 8)
print(other_list)