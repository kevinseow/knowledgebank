# constructor of LinkedList
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            # print('id(temp)', id(temp))
            temp = temp.next
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:  # this part used for case where LinkedList is empty, which shouldn't happen actually.
            self.head = new_node
            self.tail = new_node    
        else:
            self.tail.next = new_node
            # print('id(self.tail):', id(self.tail))
            self.tail = new_node
            # print('id(self.tail) after reassignment:', id(self.tail))
        self.length +=1
        return True # this line is needed for a future additional function.

    # my own implementation of pop (this should be correct)
    def pop_kev(self): 
        if self.length == 1:
            popped = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return popped.value
        elif self.length == 2:
            popped = self.tail
            self.tail = self.head
            self.head.next = None
            self.length -=1
            return popped.value
        elif self.length >= 3:
            temp = self.head
            while temp is not None:
                holder = temp.next
                if holder.next is None:
                    popped = holder
                    temp.next = None
                    self.tail = temp
                    self.length -=1
                    return popped.value
                
                else:
                    temp = temp.next

    # my 2nd iteration of pop, after watching the video (should be right too)
    def pop_kev2(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            popped = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return popped.value
        else:
            temp = self.head
            pre = self.head
            while temp is not None:
                if temp.next is not None:
                    pre = temp
                    temp = temp.next
                else:
                    self.tail = pre
                    self.tail.next = None
                    self.length -= 1
                    return temp.value

    # actual implementation of pop
    def pop(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            pre = self.head
            while temp.next: # or can use while temp.next is not None
                pre = temp
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1
        if self.length == 0: # for the edge case when LinkedList had 1 node
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1  
        return True # added because we need to use later

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length-= 1
        if self.length == 0: # for edge case where LinkedList had 1 node
            self.tail = None

        return temp

    def get_kev(self, index):
        if index < 0 or self.length <= index:
            return None
        counter = 0
        temp = self.head
        while temp is not None:
            if counter == index:
                return temp
            temp = temp.next
            counter +=1
    
    def get(self, index):
        if index < 0 or self.length <= index:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp: # or write as `if temp is not None`
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or self.length < index:
            return False # when unsuccesful, returns False
        elif index == 0:
            return self.prepend(value) # will return True as well
        elif index == self.length:
            return self.append(value) # will return True as well
        new_node = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True  # when successful, returns True

    def remove(self, index):
        if index < 0 or self.length <= index:
            return None # when unsuccesful, returns the node
        elif index == 0:
            return self.pop_first() # will return node too
        elif index == self.length - 1:
            return self.pop() # will return node too
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp  # when successful, returns True

    def reverse(self):
        pre = self.head
        temp = pre.next
        self.head = self.tail
        self.tail = pre
        self.tail.next = None
        while temp is not None:
            post = temp.next
            temp.next = pre
            pre = temp
            temp = post
            


if __name__ == '__main__':
    my_linked_list = LinkedList(1)
    my_linked_list.append(2)
    my_linked_list.append(3)
    my_linked_list.append(4)
    my_linked_list.append(5)

    my_linked_list.print_list()

    my_linked_list.reverse()

    my_linked_list.print_list()