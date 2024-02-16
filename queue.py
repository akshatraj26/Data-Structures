'''

Write a program that implements a queue data structure of specified size. If the queue becomes full 
and we try to add an element to it, then a user-defined QueueError exception should be raised.
Similarly, if the queue is empty and we try to delete an element from it then a QueueError should be raised. 

 '''

class QueueError(Exception):
    def __init__(self, msg, front, rear):
        self.errmsg = msg + 'front = ' + str(front) + 'rear=' + str(rear)
        
    def get_message(self):
        return self.errmsg
    
class Queue:
    
