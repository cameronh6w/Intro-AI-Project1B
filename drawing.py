import pygame, sys
import graphing
import networkx as nx
import random

def draw_preset_graph(screen):
    lat_lon = graphing.create_preset_graph()

    edges = graphing.get_edges()

    for edge in edges:

        start_node = int(edge[0])-1
        end_node =  int(edge[1])-1
        start_x= lat_lon[start_node][3]+300
        start_y = lat_lon[start_node][4]+600
        end_x= lat_lon[end_node][3]+300
        end_y = lat_lon[end_node][4]+600

        pygame.draw.line(screen, "Black", (start_x, start_y), (end_x,end_y), 2)

    for node in lat_lon:
        x= node[3]+300
        y = node[4]+600

        pygame.draw.circle(screen, "Blue", (x,y), 7)
        
        node_t = pygame.font.Font(None, 7).render(node[0], True, "White")
        node_r = node_t.get_rect(center=(x,y))
        screen.blit(node_t, node_r)
    


def get_random_graph_pos(G):
    nodes = list(G.nodes)
    nodes_with_pos = []
    for n in nodes:
        x= round(random.uniform(160, 800),3)
        y = round(random.uniform(180, 600),3)
        this_node = [n, x, y]
        nodes_with_pos.append(this_node) 
    return nodes_with_pos 

def draw_random_graph(screen):   
    G= graphing.create_random_graph(10,2,[1,10]) 
    
    nodes_with_pos = get_random_graph_pos(G)
    for n in nodes_with_pos:
        x = n[1]
        y = n[2]
        pygame.draw.circle(screen, "Blue", (x,y), 7)

    edges = list(G.edges)
    
    for edge in edges:
        start_node = int(edge[0])-1
        end_node =  int(edge[1])-1

        start_x= nodes_with_pos[start_node][1]
        start_y = nodes_with_pos[start_node][2]
        end_x= nodes_with_pos[end_node][1]
        end_y = nodes_with_pos[end_node][2]

        

        pygame.draw.line(screen, "Black", (start_x, start_y), (end_x,end_y), 2)
          

