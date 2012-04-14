__author__ = 'oleksandrkorobov'

import threading
import sys



class Calc_thread(threading.Thread):
    def __init__ (self):
        threading.Thread.__init__(self)
        threading.stack_size(6710886400)
        sys.setrecursionlimit(2 ** 30)
    def run(self):
        print "Calculation with recursion limit:", sys.getrecursionlimit()
        do_calculation()


class Node:
    def __init__(self, index):
        self.edges = []
        self.index = index
        self.enter_time = -1
        self.exit_time = -1
        self.processed = False
        self.discovered = False

class Graph:
    nodes = {}

    def __process_line(self, line):
        verts = line.strip("\n ").split(" ")
        node = self.nodes[int(verts[0])]
        target = self.nodes[int(verts[1])]
        node.edges.append(target)

    def __init__(self, path, v_count):
        self.nodes = dict(map(lambda number: (number + 1, Node(number + 1)), range(v_count)))

        for line in open(path, "r").readlines():
            self.__process_line(line)
        pass

def do_calculation():
    graph = Graph("./dev_scc.txt", 8)
    # Do all calculation here


calc_thread = Calc_thread()

calc_thread.start()