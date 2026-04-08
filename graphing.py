#   python3 -u "/Users/cameroncianciolo/Documents/GitHub/Intro-AI-Project1B/graphing.py"

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

import csv
import math
import random



def get_preset_graph_lat_lon():

    G = nx.Graph() 

    #collect latitude and longittude in this array  as  we  parse  csv
    lat_lon =  []
    
    #based on data
    min_lat=  38.9253  
    min_lon=  -94.716 
    max_lat=  39.3054
    max_lon= -94.5177

    with open('assets/kc_landmarks_nodes-1.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader) #skip  first line

        for row in reader:
            x = (float(row[4])-min_lon)*1000
            y = -(float(row[3])-min_lat)*1000
            
            # each line has [node id, lat, lon, adjusted x, adjusted y]
            this_node = [row[0],float(row[3]),  float(row[4]), round(x,3), round(y,3)]
            lat_lon.append(this_node)

           
            #create node
            G.add_node(row[0], label=row[3])

    with open('assets/kc_landmarks_edges-1.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader) #skip first  line 
        
        for row in reader: 
            start = int(row[0])
            end = int(row[1])
            
            lat1 = lat_lon[start-1][1]
            lon1 = lat_lon[start-1][2]

            lat2 = lat_lon[end-1][1]
            lon2 = lat_lon[end-1][2]

            distance = haversine(lat1, lon1, lat2, lon2)
    
            #create edge
            G.add_edge(row[0], row[1], weight =  round(distance, 3))

    adj_matrix = nx.to_numpy_array(G)

    return lat_lon



def create_preset_graph():

    G = nx.Graph() 

    #collect latitude and longittude in this array  as  we  parse  csv
    lat_lon =  []
    
    #based on data
    min_lat=  38.9253  
    min_lon=  -94.716 
    max_lat=  39.3054
    max_lon= -94.5177

    with open('assets/kc_landmarks_nodes-1.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader) #skip  first line

        for row in reader:
            x = (float(row[4])-min_lon)*1000
            y = -(float(row[3])-min_lat)*1000
            
            # each line has [node id, lat, lon, adjusted x, adjusted y]
            this_node = [row[0],float(row[3]),  float(row[4]), round(x,3), round(y,3)]
            lat_lon.append(this_node)

           
            #create node
            #G.add_node(row[0], label=row[3])
            G.add_node(row[0])

    with open('assets/kc_landmarks_edges-1.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader) #skip first  line 
        
        for row in reader: 
            start = int(row[0])
            end = int(row[1])
            
            lat1 = lat_lon[start-1][1]
            lon1 = lat_lon[start-1][2]

            lat2 = lat_lon[end-1][1]
            lon2 = lat_lon[end-1][2]

            distance = haversine(lat1, lon1, lat2, lon2)
    
            #create edge
            G.add_edge(row[0], row[1], weight =  round(distance, 3))

    adj_matrix = nx.to_numpy_array(G)

    return G


def get_edges():
    edges = []
    with open('assets/kc_landmarks_edges-1.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader) #skip first  line 
        
        for row in reader: 
            this_edge = [row[0], row[1]]
            edges.append(this_edge)

    return edges



         
# code is from google search ai, prompt ="how to generate a random networkx graph based on branching factor and weight distribution"
def create_random_graph(num_nodes,  b_factor, weight_distribution):

    # 1. Calculate probability 'p' from average branching factor (k)
    # p = k / (n - 1)
    p = b_factor / (num_nodes - 1)
    
    # 2. Generate Random Graph (Erdos-Renyi)
    G = nx.fast_gnp_random_graph(num_nodes, p, directed=False)

    
    # 3. Assign Weights
    for (u, v) in G.edges():
        # Option A: Uniform Distribution
        G.edges[u, v]['weight'] = round(random.uniform(weight_distribution[0], weight_distribution[1]),3)
       
        # Option B: Gaussian Distribution (comment out A if using this)
        # G.edges[u, v]['weight'] = max(0, random.gauss(0.5, 0.1))

    return G

#grid code is from my program 1
def create_random_grid(size, percent):
    total_spots = size * size
    board_matrix = create_board(size)

    #prints board with 30% blocked spots
    print(board_matrix)

    #create a matrix that's compatible to the netwrokx  graph
    graph_matrix = create_graph_matrix(size,board_matrix)

    G = nx.from_numpy_array(graph_matrix, create_using=nx.DiGraph())

#PRE: board_size must be between 3 and 10
#POST: returns a matrix for the board that contains 30% blocked spots  
def create_board(board_size):
    board_matrix = np.zeros((board_size,board_size))
    total_spots = board_size * board_size

    #   decide how many spaces to block
    percent_fill = int(total_spots * .333)

    #   get a list of blocked spaces on the board 
    blocked_spots = np.zeros(total_spots)
    for i in range(percent_fill):
        blocked_spot = random.randint(0, total_spots-1)
        blocked_spots[blocked_spot] = 1

    #   fill board with blocked spaces
    b_index = 0
    open_spots_count =0
    for i in range(board_size):
        for j in range(board_size):
            if(blocked_spots[b_index]==1):
                board_matrix[i][j] = 1
            else:
                open_spots_count = open_spots_count+1
            b_index = b_index+1

    #return result
    return board_matrix
    
#PRE:   board_size must be between 3 and 10
#       board_matrix must not be null
#POST:  returns a matrix where the  collumns and rows represent each board location
#       if the value in the cell is 1, there is a directted edge between those nodes 
#       if the value in the cell is 0, there is no edge between those nodes 
def create_graph_matrix(board_size, board_matrix):
    #   create a matrix with the rows and  collumns the length of the total amount of spots
    total_spots = board_size * board_size
    graph_matrix = np.zeros((total_spots,total_spots))


    #   look at each board space individually and identify it's neighbors 
    graph_index = 0 
    for i in range(board_size):
        for j in range(board_size):
            
            
            #   all indexes start as -1 unless a connection exists
            north_index = -1
            east_index = -1
            south_index = -1
            west_index =  -1


            #   if there exists a spot north
            if(i>0):
                north_index = board_matrix[i-1][j]
            
            #   if there exists a spot south
            if(i<board_size-1):
                south_index = board_matrix[i+1][j]
            
            #   if there exists a spot east
            if(j>0):
                east_index =  board_matrix[i][j-1]

            #   if there exists a spot west
            if(j<board_size-1):
                west_index =  board_matrix[i][j+1]

            #by the end, the current index has all it's neighboring connections

            #   if current spot isn't 1 (blocked)  or -1 (non-existant)
            if(board_matrix[i][j] == 0):

                #   fill graph matrix with 1 where there is a directed connection 
                if(north_index == 0):
                    graph_matrix[graph_index][graph_index-(board_size)] = 1
                if(east_index == 0):
                    graph_matrix[graph_index][graph_index-1] = 1
                if(south_index == 0):
                    graph_matrix[graph_index][graph_index+(board_size)] = 1
                if(west_index == 0):
                    graph_matrix[graph_index][graph_index+1] = 1
                
            #increase index each time
            graph_index = graph_index+1

    return graph_matrix

#code is from google search ai, prompt = "distance calculation for two long and lat values in python"
def haversine(lat1, lon1, lat2, lon2):
    # Radius of Earth in kilometers
    r = 6371.0
    
    # Convert degrees to radians
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * \
        math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    return r * c

def visualize_graph(G):
    # Draw the graph
    pos = nx.spring_layout(G)


    # 3. Draw nodes, edges, and standard labels
    nx.draw(G, pos, with_labels=True, node_size=100)

    # 4. Extract and draw edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)


    plt.show()



