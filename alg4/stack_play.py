__author__ = 'oleksandrkorobov'

depth = 0

import sys
import threading

threading.stack_size(6710886400)
sys.setrecursionlimit(2 ** 30)

def thread_body(n):
    print n
    #thread_body(n+1)

class Background_thread(threading.Thread):
    def __init__ (self):
        threading.Thread.__init__(self)
    def run(self):
        print sys.getrecursionlimit()



bt = Background_thread()

bt.start()