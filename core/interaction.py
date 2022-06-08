from multiprocessing import Process,Queue
from queue import Empty
import os
import time
import random
from core import actions
from core.act_queue import q as queueA
from core.cloud import cli
from core import status
# from core.cloud import connected as WEB_CONNECTED
# from core.cloud import chosen as WEB_CHOSEN



def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def ff(qI):
    queueA.put(qI)
    print("queue size####################################################",queueA.qsize())

    


def start_processes():
    print("start processes")
    p = Process(target=cli.start, args=())
    p.daemon=True
    p.start()
    pass
    
def randomAct():
    t=random.randint(0, 8)
    # # t=0
    if(status.selected):
        if t==1:
            # print("StTTTTands")
            p = Process(target=ff, args=(actions.stand(),))
            p.daemon=True
            p.start()
        if t==2:
            p = Process(target=ff, args=(actions.boring(),))
            p.daemon=True
            p.start()
        if t==3:
            p = Process(target=ff, args=(actions.lie(),))
            p.daemon=True
            p.start()
        if t==4:
            p = Process(target=ff, args=(actions.pull(),))
            p.daemon=True
            p.start()
        if t==5:
            p = Process(target=ff, args=(actions.run(),))
            p.daemon=True
            p.start()
        if t==6:
            p = Process(target=ff, args=(actions.sing(),))
            p.daemon=True
            p.start()
        if t==7:
            p = Process(target=ff, args=(actions.board(),))
            p.daemon=True
            p.start()
        if t==8:
            p = Process(target=ff, args=(actions.walkl(),))
            p.daemon=True
            p.start()
        if t==9:
            p = Process(target=ff, args=(actions.walkr(),))
            p.daemon=True
            p.start()
        # if t>=10:
        #     p = Process(target=ff, args=(actions.hide(),))
        #     p.daemon=True
        #     p.start()        
        print("randomAct")
    else:
        p = Process(target=ff, args=(actions.hide(),))
        p.daemon=True
        p.start()            



    # currentMovie = random.choice(self.allActions)
def nothingToDo(father):
    randomAct()
    # q.put(actions.walk(father))
    print("nothingToDo")
    # currentMovie = random.choice(self.allActions)

    # time.sleep(6)
    # print(q.get())    # prints "[42, None, 'hello']"
    
#     try:
#         print(q.get(block=False))    # prints "[42, None, 'hello']"
#     except Empty:
#          print("clean")
#     # p.join()
# a()