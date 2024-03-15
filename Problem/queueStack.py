# Enter your code here. Read input from STDIN. Print output to STDOUT

import os
import sys

class QueueStack:
    def __init__(self):
        self.stack1 =[]

    def enqueue(self, data):
        self.stack1.append(data)

    def dequeue(self):
        if len(self.stack1) > 0:
            #self.stack2 = [self.stack1[i] for i in range(1, len(self.stack1))]
            self.stack1 = self.stack1[1:]

    def printvalue(self):
        return self.stack1[0]

if __name__ == '__main__':
    try:
        queue = QueueStack()
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

        no_queries = int(input().strip())
        for t_itr in range(no_queries):
            command =input().strip().split()
            if len(command) == 2:
                command, value = command
                queue.enqueue(value)
            else:
                if int(command[0]) == 2:
                    queue.dequeue()
                elif int(command[0]) == 3:
                    fptr.write(queue.stack1[0] + '\n')

    except:
        print("Invalid Command")

    fptr.close()