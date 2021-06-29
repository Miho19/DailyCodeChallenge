
import logging
import time


def print_args(*args):
    for arg in args:
        logging.info("arg = %s", arg)


class Process:
    def __init__(self, function, *args):
        self.function = function
        self.args = args
        self.complete = 0
        
    def run(self):
        self.complete = 0
        self.function(self.args)
        self.complete = 1
    
class Scheduler:
    def __init__(self):
        self.index = 0
        self.tasks = list()
    
    def add(self, task: Process, delay):
        
        if task is None or delay < 0:
            return
        
        if task.function is None:
            return
        
        self.tasks.append((task, delay))
    
    def run(self):
        if len(self.tasks) == 0:
            exit()
        
        task = self.tasks[self.index]
        time.sleep(task[1])
        task[0].run()

        if task[0].complete == 1:
            self.tasks.remove(task)
        if(len(self.tasks) > 0):
            self.index = (self.index + 1) % len(self.tasks)
        else:
            exit()
        




if __name__ == "__main__":
    
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    sch = Scheduler()
    tasks = [Process(print_args, 1 , 2, 3), Process(print_args, 4, 5, 6)]

    for task in tasks:
        sch.add(task, 2)
    
    while(1):
        sch.run()
        time.sleep(1)
        
    

