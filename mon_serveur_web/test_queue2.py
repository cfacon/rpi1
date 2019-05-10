from Queue import Queue 
from threading import Thread 
import time 
class ThreadWorker(object): 
    verbose = True 
    thread = None 
    queue = Queue() 

    def __init__(self, workerId, queueMaxSize = 50, emptyQueuewaitTime = 1): 
     self.queue = Queue()
     self.queue.maxsize = queueMaxSize 
     self.thread = Thread(target=self.__work, args=(workerId, emptyQueuewaitTime)) 
     self.thread.setDaemon(True) 
     self.thread.start() 

    def __work(self, workerId, sl): 
     while(True): 
      d = self.queue.get() 
      time.sleep(1)
      self.queue.task_done() 

    def put(self, item, waitIfFull = True): 
     self.queue.put(item, waitIfFull) 
     if self.verbose: 
      print "Add to queue, current queue size: {}".format(self.queue.qsize()) 


t = ThreadWorker("t1")
t.put("item1")
t.put("item2")
t.put("item3")
