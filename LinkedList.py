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
        # add the data to the end of the linked list
        pass
    
    def insert_after(self, data, after_data):
        # iterate until after_data is found, and insert the data next in line past the after_data
        # if after_data is not found, insert at end
        pass

my_list = LinkedList()
print('list should be empty:', my_list)
my_list.insert_front(1)
my_list.insert_front(2)
my_list.insert_front(3)
print("list len:", len(my_list))
print(my_list)
# print(my_list.head, my_list.head.next, my_list.head.next.next, my_list.head.next.next.next)