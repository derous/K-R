__author__ = 'oleksandrkorobov'

import threading
import sys


class Calc_thread(threading.Thread):

    def __init__ (self):
        threading.Thread.__init__(self)
        threading.stack_size(67108864)
        sys.setrecursionlimit(2 ** 30)
    def run(self):
        print "Calculation with recursion limit:", sys.getrecursionlimit()
        do_calculation()

class Node:
    def __init__(self, index):
        self.edges = []
        self.index = index
        self.processed = False
        self.discovered = False
        self.parent = None

class Graph:
    nodes = {}

    def __process_line(self, line, is_revers_order):
        verts = line.strip("\n ").split(" ")
        if is_revers_order:
            node = self.nodes[int(verts[1])]
            target = self.nodes[int(verts[0])]
        else:
            node = self.nodes[int(verts[0])]
            target = self.nodes[int(verts[1])]
        node.edges.append(target)

    def __init__(self, path, is_revers_order, v_count):
        self.nodes = dict(map(lambda number: (number + 1, Node(number + 1)), range(v_count)))

        for line in open(path, "r").readlines():
            self.__process_line(line, is_revers_order)
        pass

nodes_stack = []

def depth_first(v):
    global nodes_stack
    v.discovered = True

    for target in v.edges:
        if not target.discovered:
            target.parent = v
            depth_first(target)
    v.processed = True

    nodes_stack.append(v.index)



def do_calculation():
    global nodes_stack
    #graph = Graph("./dev_scc.txt", 8)

    #graph = Graph("./dev_scc.txt", False, 10)
    #graph_tr = Graph("./dev_scc.txt", True, 10)

    graph = Graph("./SCC.txt", False, 875714)
    graph_tr = Graph("./SCC.txt", True, 875714)

    # Calculating order of nodes

    print "Calculating order of nodes"
    counter_ = 0
    in_element = 1379
    left = graph.nodes.keys()
    while len(left) > 0:
        depth_first(graph.nodes[in_element])
        left = filter(lambda n: not graph.nodes[n].discovered, left)
        if len(left) > 0:
            in_element = left[0]
        if counter_%100 == 0:
            print len(left)
        counter_ += 1
    pass

    print "Order calculating is finished"

    old_node_stack = list(nodes_stack)

    SCCs = []
    result_file = open("res.txt", "w")
    # Calculating SCCs

    print "Calculating SCCs"
    counter_ = 0
    while len(old_node_stack) > 0:
        nodes_stack = []
        in_element = old_node_stack[-1]
        depth_first(graph_tr.nodes[in_element])

        old_node_stack = filter( lambda n: n not in nodes_stack, old_node_stack)

        if counter_%100 == 0:
            print len(old_node_stack)
        counter_ += 1

        #print old_node_stack, "====", nodes_stack
        l = len(nodes_stack)
        if l>1:
            SCCs.append(l)
            result_file.write(str(l)+"\n")
        if l>2:
            print "l=", l

calc_thread = Calc_thread()

calc_thread.start()