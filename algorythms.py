# python3 -u "/Users/cameroncianciolo/Documents/GitHub/Intro-AI-Project1B/algorythms.py"
import networkx as nx
import queue
import graphing
import matplotlib.pyplot as plt

import heapq



def run_BFS(G, start, end):

    #create a graph that represents only what the agent at the starting position can see
    A = nx.Graph()
    A.add_node(start)

    #   order will keep track of the order that spots are seen by the agent as it searches the board
    order = []
    
    branching_factor=0 
    branching_factor_list = []  #b max and av
    nodes_generated = 0
    nodes_expanded = 0

    visited = set()


    #   current will be the node that  the player is at
    current = start
    nodes_expanded += 1 
    #   visible will keep track of all of the spots the agenntt has seen, but not visited yet
    visible = queue.Queue()
    #   start order at the starting spot
    order.append(current)
  

    #Add the starting position's nearest nodes to the graph before the loop begins
    children = G.neighbors(current)
    for i in list(children):
        if i not in visited:
            visible.put(i)
            visited.add(i)
            nodes_generated += 1
        #visible.put(i)
        #nodes_generated +=1

        #TODO test this in the loop
        A.add_node(i)
        weight = G[current][i]['weight']
        A.add_edge(current, i, weight=weight)
       

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
            weight = G[current][end]['weight']
            A.add_edge(current, end, weight=weight)
            
            
            order.append(end)
           
               
            #clear queue
            while not visible.empty():
                visible.get()
                
            
            #end loop
            break
        
        #   set the new visted node to the next visible spot in the queue (and remove that spot from the qeue)
        current = visible.get()
        nodes_expanded += 1
        

        #   add the current position's nearest nodes to the graph  and visible queue
        children = G.neighbors(current)
        for i in list(children):
            if i not in visited:
                visible.put(i)
                visited.add(i)
                nodes_generated += 1
            #visible.put(i)
            #nodes_generated += 1
            A.add_node(i)
            weight = G[current][i]['weight']
            A.add_edge(current, i, weight=weight)
            
            if(i not in order):
                order.append(i)
              
                
                

            branching_factor =  branching_factor+1
        branching_factor_list.append(branching_factor)
        branching_factor = 0

           

    #when all  spots have been visited or shortest path was  found,  use networkx library to get the shortest path
    shortest_path_found = nx.shortest_path(A, source=start, target=end, weight='weight')
    shortest_path_actual = nx.shortest_path(G, source=start, target=end, weight='weight')

    shortest_path_cost_found = nx.shortest_path_length(A, source=start, target=end, weight='weight')
    shortest_path_cost_actual = nx.shortest_path_length(G, source=start, target=end, weight='weight')
    
    shortest_path_depth= len(shortest_path_found)-1
    max_b_fact =  max(branching_factor_list)
    avg_b_fact = round(sum(branching_factor_list) / len(branching_factor_list),3)

    stats = [order, "BFS", shortest_path_found, shortest_path_cost_found, shortest_path_actual,shortest_path_cost_actual,shortest_path_depth,max_b_fact,avg_b_fact, nodes_expanded, nodes_generated]
    print(stats)
    return stats

def run_DFS(G, start, end):

    # Graph of what the agent has "seen"
    A = nx.Graph()
    A.add_node(start)

    order = []

    branching_factor = 0
    branching_factor_list = []

    nodes_expanded=0
    nodes_generated=0

    # Stack instead of queue
    stack = []
    visited = set()

    # Start
    stack.append(start)
    nodes_generated +=1
    visited.add(start)
    order.append(start)

    while stack:
        current = stack.pop()
        nodes_expanded +=1

        # If goal found, stop
        if current == end:
            break

        children = list(G.neighbors(current))
        branching_factor = 0

        for neighbor in children:
            # Build visible graph A
            A.add_node(neighbor)
            weight = G[current][neighbor]['weight']
            A.add_edge(current, neighbor, weight=weight)
            #A.add_edge(current, neighbor)

            if neighbor not in visited:
                stack.append(neighbor)
                nodes_generated +=1
                visited.add(neighbor)
                order.append(neighbor)
                branching_factor += 1

        branching_factor_list.append(branching_factor)
      

    # --- Shortest path on discovered graph ---
    shortest_path_found = nx.shortest_path(A, source=start, target=end, weight='weight')
    shortest_path_actual = nx.shortest_path(G, source=start, target=end, weight='weight')

    shortest_path_cost_found = round(nx.shortest_path_length(A, source=start, target=end, weight='weight'),3)
    shortest_path_cost_actual = round(nx.shortest_path_length(G, source=start, target=end, weight='weight'),3)

    shortest_path_depth = len(shortest_path_found) - 1

    # --- Stats ---
    if len(branching_factor_list) > 0:
        max_b_fact = max(branching_factor_list)
        avg_b_fact = round(sum(branching_factor_list) / len(branching_factor_list),3)
    else:
        max_b_fact = 0
        avg_b_fact = 0

    stats = [order, "DFS",shortest_path_found, shortest_path_cost_found, shortest_path_actual,shortest_path_cost_actual,shortest_path_depth,max_b_fact,avg_b_fact, nodes_expanded, nodes_generated]
    print(stats)
    return stats

def run_IDDFS(G, start, end):

    A = nx.Graph()
    A.add_node(start)

    order = []

    branching_factor_list = []

    nodes_expanded = 0
    nodes_generated = 0

    found = False
    depth_limit = 0

    # --- Depth-Limited DFS ---
    def dls(node, depth, visited):
        nonlocal nodes_expanded, nodes_generated, found

        if found:
            return

        nodes_expanded += 1

        if node not in order:
            order.append(node)

        if node == end:
            found = True
            return

        if depth == 0:
            return

        children = list(G.neighbors(node))
        branching_factor = 0

        for neighbor in children:
            # build graph A with weights
            A.add_node(neighbor)
            weight = G[node][neighbor]['weight']
            A.add_edge(node, neighbor, weight=weight)

            nodes_generated += 1
            branching_factor += 1

            if neighbor not in visited:
                visited.add(neighbor)
                dls(neighbor, depth - 1, visited)

        branching_factor_list.append(branching_factor)

    # --- IDDFS Loop ---
    while not found:
        visited = set()
        visited.add(start)

        dls(start, depth_limit, visited)

        depth_limit += 1

    # --- Shortest paths ---
    shortest_path_found = nx.shortest_path(A, source=start, target=end, weight='weight')
    shortest_path_actual = nx.shortest_path(G, source=start, target=end, weight='weight')

    shortest_path_cost_found = round(nx.shortest_path_length(A, source=start, target=end, weight='weight'), 3)
    shortest_path_cost_actual = round(nx.shortest_path_length(G, source=start, target=end, weight='weight'), 3)

    shortest_path_depth = len(shortest_path_found) - 1

    # --- Stats ---
    if branching_factor_list:
        max_b_fact = max(branching_factor_list)
        avg_b_fact = round(sum(branching_factor_list) / len(branching_factor_list), 3)
    else:
        max_b_fact = 0
        avg_b_fact = 0

    stats = [
        order,
        "IDDFS",
        shortest_path_found,
        shortest_path_cost_found,
        shortest_path_actual,
        shortest_path_cost_actual,
        shortest_path_depth,
        max_b_fact,
        avg_b_fact,
        nodes_expanded,
        nodes_generated
    ]

    print(stats)
    return stats


def run_Greedy(G, start, end):

    A = nx.Graph()
    A.add_node(start)

    order = []

    branching_factor_list = []

    nodes_expanded = 0
    nodes_generated = 0

    visited = set()

    # --- Heuristic (straight-line distance) ---
    def heuristic(n1, n2):
        # assuming your graph nodes map to lat/lon like preset graph
        lat_lon = graphing.get_preset_graph_lat_lon()

        i1 = int(n1) - 1
        i2 = int(n2) - 1

        lat1, lon1 = lat_lon[i1][1], lat_lon[i1][2]
        lat2, lon2 = lat_lon[i2][1], lat_lon[i2][2]

        return graphing.haversine(lat1, lon1, lat2, lon2)

    # priority queue: (heuristic, node)
    pq = []
    heapq.heappush(pq, (heuristic(start, end), start))
    nodes_generated += 1

    visited.add(start)
    order.append(start)

    while pq:
        _, current = heapq.heappop(pq)
        nodes_expanded += 1

        if current == end:
            break

        children = list(G.neighbors(current))
        branching_factor = 0

        for neighbor in children:

            # build graph A with weights
            A.add_node(neighbor)
            weight = G[current][neighbor]['weight']
            A.add_edge(current, neighbor, weight=weight)

            if neighbor not in visited:
                priority = heuristic(neighbor, end)
                heapq.heappush(pq, (priority, neighbor))
                nodes_generated += 1

                visited.add(neighbor)
                order.append(neighbor)
                branching_factor += 1

        branching_factor_list.append(branching_factor)

    # --- shortest paths ---
    shortest_path_found = nx.shortest_path(A, source=start, target=end, weight='weight')
    shortest_path_actual = nx.shortest_path(G, source=start, target=end, weight='weight')

    shortest_path_cost_found = round(nx.shortest_path_length(A, source=start, target=end, weight='weight'), 3)
    shortest_path_cost_actual = round(nx.shortest_path_length(G, source=start, target=end, weight='weight'), 3)

    shortest_path_depth = len(shortest_path_found) - 1

    # --- stats ---
    if branching_factor_list:
        max_b_fact = max(branching_factor_list)
        avg_b_fact = round(sum(branching_factor_list) / len(branching_factor_list), 3)
    else:
        max_b_fact = 0
        avg_b_fact = 0

    stats = [
        order,
        "Greedy",
        shortest_path_found,
        shortest_path_cost_found,
        shortest_path_actual,
        shortest_path_cost_actual,
        shortest_path_depth,
        max_b_fact,
        avg_b_fact,
        nodes_expanded,
        nodes_generated
    ]

    print(stats)
    return stats



import heapq

def run_Astar(G, start, end):

    A = nx.Graph()
    A.add_node(start)

    order = []

    branching_factor_list = []

    nodes_expanded = 0
    nodes_generated = 0

    visited = set()

    # --- Heuristic (same as Greedy) ---
    def heuristic(n1, n2):
        lat_lon = graphing.get_preset_graph_lat_lon()

        i1 = int(n1) - 1
        i2 = int(n2) - 1

        lat1, lon1 = lat_lon[i1][1], lat_lon[i1][2]
        lat2, lon2 = lat_lon[i2][1], lat_lon[i2][2]

        return graphing.haversine(lat1, lon1, lat2, lon2)

    # priority queue: (f, g, node)
    pq = []
    heapq.heappush(pq, (heuristic(start, end), 0, start))
    nodes_generated += 1

    # cost so far
    g_cost = {start: 0}

    order.append(start)

    while pq:
        f, current_g, current = heapq.heappop(pq)

        # avoid re-expanding worse paths
        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current == end:
            break

        children = list(G.neighbors(current))
        branching_factor = 0

        for neighbor in children:

            weight = G[current][neighbor]['weight']
            new_g = current_g + weight

            # build graph A
            A.add_node(neighbor)
            A.add_edge(current, neighbor, weight=weight)

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g

                f_score = new_g + heuristic(neighbor, end)
                heapq.heappush(pq, (f_score, new_g, neighbor))
                nodes_generated += 1

                if neighbor not in order:
                    order.append(neighbor)

                branching_factor += 1

        branching_factor_list.append(branching_factor)

    # --- shortest paths ---
    shortest_path_found = nx.shortest_path(A, source=start, target=end, weight='weight')
    shortest_path_actual = nx.shortest_path(G, source=start, target=end, weight='weight')

    shortest_path_cost_found = round(nx.shortest_path_length(A, source=start, target=end, weight='weight'), 3)
    shortest_path_cost_actual = round(nx.shortest_path_length(G, source=start, target=end, weight='weight'), 3)

    shortest_path_depth = len(shortest_path_found) - 1

    # --- stats ---
    if branching_factor_list:
        max_b_fact = max(branching_factor_list)
        avg_b_fact = round(sum(branching_factor_list) / len(branching_factor_list), 3)
    else:
        max_b_fact = 0
        avg_b_fact = 0

    stats = [
        order,
        "A*",
        shortest_path_found,
        shortest_path_cost_found,
        shortest_path_actual,
        shortest_path_cost_actual,
        shortest_path_depth,
        max_b_fact,
        avg_b_fact,
        nodes_expanded,
        nodes_generated
    ]

    print(stats)
    return stats