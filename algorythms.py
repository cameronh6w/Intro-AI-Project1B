# python3 -u "/Users/cameroncianciolo/Documents/GitHub/Intro-AI-Project1B/algorythms.py"
import networkx as nx
import queue
import graphing
import matplotlib.pyplot as plt


def run_BFS(G, start, end):

    #create a graph that represents only what the agent at the starting position can see
    A = nx.Graph()
    A.add_node(start)

    #   order will keep track of the order that spots are seen by the agent as it searches the board
    order = []
    
    branching_factor=0 
    branching_factor_list = []  #b max and av


    #   current will be the node that  the player is at
    current = start
    #   visible will keep track of all of the spots the agenntt has seen, but not visited yet
    visible = queue.Queue()
    #   start order at the starting spot
    order.append(current)
    
    


    #Add the starting position's nearest nodes to the graph before the loop begins
    children = G.neighbors(current)
    for i in list(children):
        visible.put(i)
        A.add_node(i)
        A.add_edge(current, i)

        #stats
        order.append(i)
        branching_factor =  branching_factor+1
    branching_factor_list.append(branching_factor)
    branching_factor = 0

   
    #continue to search the graph until all visble spots have been visited (or goal is found)
    while(not visible.empty()):
        
        #   if the goal is now visible, end the loop
        if(end in visible.queue):
            
            #   add all the goal into the graph, and the order
            A.add_node(end)
            A.add_edge(current, end)
            
            order.append(end)
            

            

            
            #clear queue
            while not visible.empty():
                visible.get()
            
            #end loop
            break
        
        #   set the new visted node to the next visible spot in the queue (and remove that spot from the qeue)
        current = visible.get()
        

        #   add the current position's nearest nodes to the graph  and visible queue
        children = G.neighbors(current)
        for i in list(children):
            visible.put(i)
            A.add_node(i)
            A.add_edge(current, i)
            
            if(i not in order):
                order.append(i)
                
                

            branching_factor =  branching_factor+1
        branching_factor_list.append(branching_factor)
        branching_factor = 0

           

    #when all  spots have been visited or shortest path was  found,  use networkx library to get the shortest path
    shortest_path = nx.shortest_path(A, source=start, target=end, weight='weight')
    shortest_path_cost = nx.shortest_path_length(A, source=start, target=end, weight='weight')
    shortest_path_depth= len(shortest_path)-1
    max_b_fact =  max(branching_factor_list)
    avg_b_fact = sum(branching_factor_list) / len(branching_factor_list)

    stats = [order, shortest_path, shortest_path_cost,shortest_path_depth,max_b_fact,avg_b_fact]

    return stats






def run_DFS():
    print("DFS")

def run_IDDFS():
    print("IDDFS")

def run_Greedy():
    print("Greedy")

def run_Astar():
    print("Astar")