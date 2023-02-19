# Python3 code to implement Priority Queue
# using Singly Linked List
 
# Class to create new node which includes
# Node Data, and Node Priority
class PriorityQueueNode:
     
  def __init__(self, value, pr):
       
    self.data = value
    self.priority = pr
    self.next = None
         
# Implementation of Priority Queue
class PriorityQueue:
     
    def __init__(self):
         
        self.front = None
         
    # Method to check Priority Queue is Empty
    # or not if Empty then it will return True
    # Otherwise False
    def isEmpty(self):
         
        return True if self.front == None else False
     
    # Method to add items in Priority Queue
    # According to their priority value
    def push(self, value, priority):
         
        # Condition check for checking Priority
        # Queue is empty or not
        if self.isEmpty() == True:
             
            # Creating a new node and assigning
            # it to class variable
            self.front = PriorityQueueNode(value,
                                           priority)
             
            # Returning 1 for successful execution
             return 1
             
        else:
             
            # Special condition check to see that
            # first node priority value
            if self.front.priority > priority:
                 
                # Creating a new node
                newNode = PriorityQueueNode(value,
                                            priority)
                 
                # Updating the new node next value
                newNode.next = self.front
                 
                # Assigning it to self.front
                self.front = newNode
                 
                # Returning 1 for successful execution
                return 1
                 
            else:
                 
                # Traversing through Queue until it
                # finds the next smaller priority node
                temp = self.front
                 
                while temp.next:
                     
                    # If same priority node found then current
                    # node will come after previous node
                    if priority <= temp.next.priority:
                        break
                     
                    temp = temp.next
                 
                newNode = PriorityQueueNode(value,
                                            priority)
                newNode.next = temp.next
                return 1
                 
            else:
                 
                # Traversing through Queue until it
                # finds the next smaller priority node
                temp = self.front
                 
                while temp.next:
                     
                    # If same priority node found then current
                    # node will come after previous node
                    if priority <= temp.next.priority:
                        break
                     
                    temp = temp.next
                 
                newNode = PriorityQueueNode(value,
                                            priority)
                newNode.next = temp.next