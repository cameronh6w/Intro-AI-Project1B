#  python3 -u "/Users/cameroncianciolo/Documents/GitHub/Intro-AI-Project1B/main.py"

# code from youtuber BaralTech video "HOW TO MAKE A MENU SCREEN IN PYGAME!"
import pygame, sys
from button import Button
import graphing
import networkx as nx
import random
import drawing
import algorythms
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

from pygame_widgets.dropdown import Dropdown

pygame.init()

seed = 8


screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def results(stats, is_random = False, settings = []):
    print(stats)

    search = stats[1]

    shortest_path_found = str(stats[2])
    shortest_path_cost_found= str(stats[3])

    shortest_path_actual = str(stats[4])
    shortest_path_cost_actual = str(stats[5])
    
    shortest_path_depth= str(stats[6])
    max_b_fact = str(stats[7])  
    avg_b_fact = str(stats[8])
    nodes_expanded = str(stats[9]) 

    nodes_generated= str(stats[10])


    while True:
        mouse_pos = pygame.mouse.get_pos()
        screen.fill("white")

        #title
        r_title_text = get_font(50).render("Results", True, "#b68f40")
        r_title_rect = r_title_text.get_rect(center=(640, 100))
        screen.blit(r_title_text, r_title_rect)
        
        #results text
        sa_text = get_font(20).render("Search Algorythm: "+search, True, "#000000")
        sa_rect = sa_text.get_rect(topleft=(100, 180))
        screen.blit(sa_text, sa_rect)

        sp_text = get_font(20).render("Shortest Path Found:  ", True, "#000000")
        sp_rect = sp_text.get_rect(topleft=(100, 210))
        screen.blit(sp_text, sp_rect)

        text = "    "+shortest_path_found+" - Cost: "+shortest_path_cost_found+" km"
        sp_text1 = get_font(20).render(text, True, "#b68f40")
        sp_rect1 = sp_text1.get_rect(topleft=(100, 240))
        screen.blit(sp_text1, sp_rect1)
        
        c_text = get_font(20).render("Actual Shortest Path: ", True, "#000000")
        c_rect = c_text.get_rect(topleft=(100, 270))
        screen.blit(c_text, c_rect)

        text = "    "+shortest_path_actual+" - Cost: "+shortest_path_cost_actual+" km"
        c_text1 = get_font(20).render(text, True, "#b68f40")
        c_rect1 = c_text1.get_rect(topleft=(100, 300))
        screen.blit(c_text1, c_rect1)

        d_text = get_font(20).render("Depth: "+ shortest_path_depth, True, "#000000")
        d_rect = d_text.get_rect(topleft=(100, 330))
        screen.blit(d_text, d_rect)

        mb_text = get_font(20).render("Max Branching Factor: "+max_b_fact, True, "#000000")
        mb_rect = mb_text.get_rect(topleft=(100, 360))
        screen.blit(mb_text, mb_rect)

        ab_text = get_font(20).render("Avg Branching Factor: "+avg_b_fact, True, "#000000")
        ab_rect = ab_text.get_rect(topleft=(100, 390))
        screen.blit(ab_text, ab_rect)

        ne_text = get_font(20).render("Nodes Expanded: "+nodes_expanded, True, "#000000")
        ne_rect = ne_text.get_rect(topleft=(100, 420))
        screen.blit(ne_text, ne_rect)

        ng_text = get_font(20).render("Nodes Generated: "+nodes_generated, True, "#000000")
        ng_rect = ng_text.get_rect(topleft=(100, 450))
        screen.blit(ng_text, ng_rect)


        #buttons
        r_back_button = Button(image=None, pos=(640, 660),text_input="Back", font=get_font(20), base_color="Black", hovering_color="Blue")
        r_back_button.changeColor(mouse_pos)
        r_back_button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if r_back_button.checkForInput(mouse_pos):
                    graph_visual(is_random, settings)
        pygame.display.update()

def get_order_from_search(is_random, search, G,start,end):
    order = []
    if is_random:
        if(start != None and end != None):
            if search ==1:
                order = algorythms.run_BFS(G, int(start), int(end))[0]
            if search ==2:
                order = algorythms.run_DFS(G, int(start), int(end))[0]
            if search ==3:
                order = algorythms.run_IDDFS(G, int(start), int(end))[0]
            if search ==4:
                order = algorythms.run_Greedy(G, int(start), int(end))[0]
            if search ==5:
                order = algorythms.run_Astar(G, int(start), int(end))[0]
    else:
        if(start != None and end != None):
            if search ==1:
                order = algorythms.run_BFS(G, str(start), str(end))[0]
            if search ==2:
                order = algorythms.run_DFS(G,str(start), str(end))[0]
            if search ==3:
                order = algorythms.run_IDDFS(G, str(start), str(end))[0]
            if search ==4:
                order = algorythms.run_Greedy(G, str(start), str(end))[0]
            if search ==5:
                order = algorythms.run_Astar(G, str(start), str(end))[0]

    return order


def get_stats_from_search(is_random, search, G,start,end):

    stats = []
                
    if is_random:
        if(start != None and end != None):
            if search ==1:
                stats = algorythms.run_BFS(G, int(start), int(end))
            if search ==2:
                stats = algorythms.run_DFS(G, int(start), int(end))
            if search ==3:
                stats = algorythms.run_IDDFS(G, int(start), int(end))
            if search ==4:
                stats = algorythms.run_Greedy(G, int(start), int(end))
            if search ==5:
                stats = algorythms.run_Astar(G, int(start), int(end))
    else:
        if(start != None and end != None):
            if search ==1:
                stats = algorythms.run_BFS(G, str(start), str(end))
            if search ==2:
                stats = algorythms.run_DFS(G,str(start), str(end))
            if search ==3:
                stats = algorythms.run_IDDFS(G, str(start), str(end))
            if search ==4:
                stats = algorythms.run_Greedy(G, str(start), str(end))
            if search ==5:
                stats = algorythms.run_Astar(G, str(start), str(end))

    return stats

def graph_visual(is_random = False, settings = []):
    global clock
    clock = pygame.time.Clock()

    global search 
    search = 1 #1-BFS 2-DFS 3-IDDFS 4-Gredy 5-Astar

    node_positions =[] 
    node_options= []
    node_val = []
    if(is_random):
        random.seed(seed)
        G = graphing.create_random_graph(settings[0],settings[1],[settings[2],settings[3]]) 
        node_positions = drawing.get_random_graph_pos(G)
        node_options =  [str(n) for n in G.nodes]
        node_val = list(G.nodes)
    else:
        G = graphing.create_preset_graph()
        node_positions = None
        node_options = [data['label'] for node, data in G.nodes(data=True)]
        node_val = [int(n) for n in G.nodes]

    global playing 
    playing = False
    order = []
    step_index = 0
    visited = []

    frame_counter= 0
    animation_delay = 5  # lower = faster

   

    #print(node_options)
    dropdown_start = Dropdown(
        screen, 807, 210, 250, 25, name='Select Start Node', fontSize=20,
        choices= node_options,values =node_val,
        borderRadius=1, colour=pygame.Color('grey'), direction='down', textHAlign='left'
        )
    
    dropdown_end = Dropdown(
        screen, 807, 280, 250, 25, name='Select End Node', fontSize=20,
        choices= node_options,values =node_val,
        borderRadius=1, colour=pygame.Color('grey'), direction='down', textHAlign='left'
        )
    widgets = [dropdown_start,dropdown_end]


    while True:
        
        v_mouse_pos = pygame.mouse.get_pos()
        screen.fill("white")

        #title
        v_title_text = get_font(50).render("Graph Visualization", True, "#b68f40")
        v_title_rect = v_title_text.get_rect(center=(640, 100))
        screen.blit(v_title_text, v_title_rect)

        #buttons
        v_back_button = Button(image=None, pos=(500, 660),text_input="Back to Menu", font=get_font(20), base_color="Black", hovering_color="Blue")
        v_back_button.changeColor(v_mouse_pos)
        v_back_button.update(screen)

        v_next_button = Button(image=None, pos=(780, 660),text_input="Next", font=get_font(20), base_color="Black", hovering_color="Blue")
        v_next_button.changeColor(v_mouse_pos)
        v_next_button.update(screen)

        BFS_button = Button(image=None, pos=(832, 360),text_input="BFS", font=get_font(15), base_color="Black", hovering_color="Blue")
        BFS_button.changeColor(v_mouse_pos)
        BFS_button.update(screen)

        DFS_button = Button(image=None, pos=(890, 360),text_input="DFS", font=get_font(15), base_color="Black", hovering_color="Blue")
        DFS_button.changeColor(v_mouse_pos)
        DFS_button.update(screen)

        IDDFS_button = Button(image=None, pos=(960, 360),text_input="IDDFS", font=get_font(15), base_color="Black", hovering_color="Blue")
        IDDFS_button.changeColor(v_mouse_pos)
        IDDFS_button.update(screen)

        Greedy_button = Button(image=None, pos=(1050, 360),text_input="Greedy", font=get_font(15), base_color="Black", hovering_color="Blue")
        Greedy_button.changeColor(v_mouse_pos)
        Greedy_button.update(screen)


        Astar_button = Button(image=None, pos=(1120, 360),text_input="A*", font=get_font(15), base_color="Black", hovering_color="Blue")
        Astar_button.changeColor(v_mouse_pos)
        Astar_button.update(screen)

        play_button = Button(image=None, pos=(852, 400),text_input="Play", font=get_font(20), base_color="Black", hovering_color="Blue")
        play_button.changeColor(v_mouse_pos)
        play_button.update(screen)

        pause_button = Button(image=None, pos=(860, 450),text_input="Pause", font=get_font(20), base_color="Black", hovering_color="Blue")
        pause_button.changeColor(v_mouse_pos)
        pause_button.update(screen)

        step_button = Button(image=None, pos=(851, 500),text_input="Step", font=get_font(20), base_color="Black", hovering_color="Blue")
        step_button.changeColor(v_mouse_pos)
        step_button.update(screen)

        reset_button = Button(image=None, pos=(859, 550),text_input="Reset", font=get_font(20), base_color="Black", hovering_color="Blue")
        reset_button.changeColor(v_mouse_pos)
        reset_button.update(screen)

        

        #rectangle for sections
        graph_rect = (160, 170, 640, 450) 
        pygame.draw.rect(screen, "Black", graph_rect, width=1)
         
        settings_rect = (800, 170, 320, 450) 
        pygame.draw.rect(screen, "Black", settings_rect, width=1)

        #Settings text
        start_node_text = get_font(20).render("Start Node: ", True, "#b68f40")
        start_node_rect = start_node_text.get_rect(topleft=(807, 180))
        screen.blit(start_node_text, start_node_rect)

        end_node_text = get_font(20).render("End Node: ", True, "#b68f40")
        end_node_rect = end_node_text.get_rect(topleft=(807, 250))
        screen.blit(end_node_text, end_node_rect)

        search_text = get_font(20).render("Select Search: ", True, "#b68f40")
        search_rect = search_text.get_rect(topleft=(807, 320))
        screen.blit(search_text, search_rect)

        speed_text = get_font(20).render("Speed: ", True, "#b68f40")
        speed_rect = speed_text.get_rect(topleft=(807, 585))
        screen.blit(speed_text, speed_rect)

        #from ai 
        frame_counter += 1
        
        if playing and frame_counter % animation_delay == 0:
            
            if step_index < len(order):
                visited.append(order[step_index])
                print(visited)
                step_index += 1
            else:
                playing = False
        
        #event handling
        
        if is_random:
            drawing.draw_random_graph(screen, G, node_positions, visited)
        else:
            drawing.draw_preset_graph(screen, visited)

        
          
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if v_back_button.checkForInput(v_mouse_pos):
                    hide_widgets(widgets)
                    main_menu()
                if BFS_button.checkForInput(v_mouse_pos):
                    search = 1
                if DFS_button.checkForInput(v_mouse_pos):
                    search = 2
                if IDDFS_button.checkForInput(v_mouse_pos):
                    search = 3
                if Greedy_button.checkForInput(v_mouse_pos):
                    search = 4
                if Astar_button.checkForInput(v_mouse_pos):
                    search = 5
                if play_button.checkForInput(v_mouse_pos):
                    print("PLAY CLICKED")
                    start = dropdown_start.getSelected()
                    end = dropdown_end.getSelected()
                    
                    order = get_order_from_search(is_random, search, G,start,end)

                    print("ORDER:", order)
                    playing = True
                    visited = []
                    step_index = 0
                if v_next_button.checkForInput(v_mouse_pos):
                    #run all selected algs, give them  to restults 
                    stats = get_stats_from_search(is_random, search, G,start,end)
                    
                    hide_widgets(widgets)
                    results(stats, is_random, settings)
            

        events = pygame.event.get()
        pygame_widgets.update(events)
        
        pygame.display.update()
        clock.tick(60) 
        

def random_settings_graph():
    screen.fill("white")
    nodes_slider = Slider(screen, 620, 215, 400, 20, min=2, max=30, colour="#b68f40", initial=2, step=1)
    nodes_output = TextBox(screen, 525, 205, 60, 40, fontSize=25)
    nodes_output.disable()  # Act as label instead of textbox
    nodes_slider.setValue(2)
    

    b_fact_slider = Slider(screen, 620, 265, 400, 20, min=1, max=10, colour="#b68f40", initial=1, step=1)
    b_fact_output = TextBox(screen, 525, 255, 60, 40, fontSize=25)
    b_fact_output.disable()  # Act as label instead of textbox

    dist_min_slider = Slider(screen, 620, 365, 400, 20, min=1, max=10, colour="#b68f40", initial=1, step=1)
    dist_min_output = TextBox(screen, 690, 310, 60, 40, colour ="#ffffff", borderColour="#ffffff", fontSize=25)
    dist_min_output.disable()  # Act as label instead of textbox

    dist_range_slider = Slider(screen, 620, 415, 400, 20, min=1, max=10, colour="#b68f40", initial=1, step=1)
    dist_range_output = TextBox(screen, 740, 310, 30, 40,colour ="#ffffff", borderColour="#ffffff", fontSize=25)
    dist_range_output.disable()  # Act as label instead of textbox

    widgets = [nodes_slider,nodes_output,b_fact_slider,b_fact_output,dist_min_slider,dist_min_output,dist_range_slider,dist_range_output]

    while True:
        r_mouse_pos = pygame.mouse.get_pos()
        screen.fill("white")

        #title
        r_title_text = get_font(50).render("Random Graph Settings", True, "#b68f40")
        r_title_rect = r_title_text.get_rect(center=(640, 100))
        screen.blit(r_title_text, r_title_rect)

        #button background squares
        graph_rect = (160, 160, 110, 40) 
        pygame.draw.rect(screen, "Black", graph_rect, width=1)

        grid_rect = (270, 160, 110, 40) 
        pygame.draw.rect(screen, "Grey", grid_rect)

        #buttons
        r_next_button = Button(image=None, pos=(640, 660), text_input="Next", font=get_font(20), base_color="Black", hovering_color="Blue")
        r_next_button.changeColor(r_mouse_pos)
        r_next_button.update(screen)

        graph_settings_button = Button(image=None, pos=(210, 180), text_input="Graph", font=get_font(20), base_color="Black", hovering_color="Blue")
        graph_settings_button.changeColor(r_mouse_pos)
        graph_settings_button.update(screen)

        grid_settings_button = Button(image=None, pos=(320, 180), text_input="Grid", font=get_font(20), base_color="Black", hovering_color="Blue")
        grid_settings_button.changeColor(r_mouse_pos)
        grid_settings_button.update(screen)

        seed_button = Button(image=None, pos=(640, 680), text_input="Change Seed", font=get_font(20), base_color="Black", hovering_color="Blue")
        seed_button.changeColor(r_mouse_pos)
        seed_button.update(screen)

        #rectangle for settings
        settings_rect = (160, 200, 960, 400) 
        pygame.draw.rect(screen, "Black", settings_rect, width=1)

        #Settings text
        num_nodes_text = get_font(20).render("Number of Nodes: ", True, "#b68f40")
        num_nodes_rect = num_nodes_text.get_rect(center=(345, 230))
        screen.blit(num_nodes_text, num_nodes_rect)

        b_factor_text = get_font(20).render("Branching Factor: ", True, "#b68f40")
        b_factor_rect = b_factor_text.get_rect(center=(356, 280))
        screen.blit(b_factor_text, b_factor_rect)

        e_weight_text = get_font(20).render("Edge Weight Distribution:[    ] ", True, "#b68f40")
        e_weight_rect = e_weight_text.get_rect(topleft=(176, 320))
        screen.blit(e_weight_text, e_weight_rect)

        min_weight_text = get_font(20).render("Minimum:", True, "#b68f40")
        min_weight_rect = min_weight_text.get_rect(center=(400, 380))
        screen.blit(min_weight_text, min_weight_rect)

        range_weight_text = get_font(20).render("Range: ", True, "#b68f40")
        range_weight_rect = range_weight_text.get_rect(center=(400, 430))
        screen.blit(range_weight_text, range_weight_rect)

        
        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if r_next_button.checkForInput(r_mouse_pos):
                    random_settings = [nodes_slider.getValue(),b_fact_slider.getValue(),dist_min_slider.getValue(),dist_range_slider.getValue()+dist_min_slider.getValue()]
                    print(random_settings)
                    hide_widgets(widgets)
                    graph_visual(True,random_settings)


                if grid_settings_button.checkForInput(r_mouse_pos):
                    hide_widgets(widgets)
                    random_settings_grid()
                
                if graph_settings_button.checkForInput(r_mouse_pos):

                    random_settings_graph()
                if seed_button.checkForInput(r_mouse_pos):
                    global seed
                    seed = random.randint(1, 10)

        events = pygame.event.get()
        #screen.fill("white")
        nodes_output.setText(nodes_slider.getValue())
        b_fact_output.setText(b_fact_slider.getValue())
        dist_min_output.setText(dist_min_slider.getValue())
        dist_range_output.setText(dist_range_slider.getValue()+dist_min_slider.getValue())
       
        
        pygame_widgets.update(events)
        pygame.display.update()

def hide_widgets(widgets):
    for w in widgets:
        w.hide()

def random_settings_grid():
    while True:
        r_mouse_pos = pygame.mouse.get_pos()
        screen.fill("white")

        #title
        r_title_text = get_font(50).render("Random Graph Settings", True, "#b68f40")
        r_title_rect = r_title_text.get_rect(center=(640, 100))
        screen.blit(r_title_text, r_title_rect)

        #button background squares
        graph_rect = (160, 160, 110, 40) 
        pygame.draw.rect(screen, "Grey", graph_rect)

        grid_rect = (270, 160, 110, 40) 
        pygame.draw.rect(screen, "Black", grid_rect, width=1)

        #buttons
        r_next_button = Button(image=None, pos=(640, 660), text_input="Next", font=get_font(20), base_color="Black", hovering_color="Blue")
        r_next_button.changeColor(r_mouse_pos)
        r_next_button.update(screen)

        graph_settings_button = Button(image=None, pos=(210, 180), text_input="Graph", font=get_font(20), base_color="Black", hovering_color="Blue")
        graph_settings_button.changeColor(r_mouse_pos)
        graph_settings_button.update(screen)

        grid_settings_button = Button(image=None, pos=(320, 180), text_input="Grid", font=get_font(20), base_color="Black", hovering_color="Blue")
        grid_settings_button.changeColor(r_mouse_pos)
        grid_settings_button.update(screen)

        #rectangle for  settings
        settings_rect = (160, 200, 960, 400) 
        pygame.draw.rect(screen, "Black", settings_rect, width=1)

        #Settings text
        grid_size_text = get_font(20).render("Size of grid: ", True, "#b68f40")
        grid_size_rect = grid_size_text.get_rect(center=(315, 230))
        screen.blit(grid_size_text, grid_size_rect)

        obsticles_text = get_font(20).render("Percent of obsticles: ", True, "#b68f40")
        obsticles_rect = obsticles_text.get_rect(center=(395, 280))
        screen.blit(obsticles_text, obsticles_rect)

        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if r_next_button.checkForInput(r_mouse_pos):
                    graph_visual(True)
                if grid_settings_button.checkForInput(r_mouse_pos):
                    random_settings_grid()
                if graph_settings_button.checkForInput(r_mouse_pos):
                    random_settings_graph()
                

        pygame.display.update()

def main_menu():
    while True:

        screen.fill("Black")
        menu_mouse_pos = pygame.mouse.get_pos()

        #title
        menu_text = get_font(100).render("MAIN MENU", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(640, 100))

        #buttons
        preset_button = Button(None, pos=(640, 250), text_input="Preset", font=get_font(75),base_color="#d7fcd4", hovering_color="White")
        random_button = Button(None, pos=(640, 400), text_input="Random", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        quit_button = Button(None,pos=(640, 550), text_input="Quit", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(menu_text, menu_rect)

        #change color if hovering over
        for button in [preset_button, random_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)
        
        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if preset_button.checkForInput(menu_mouse_pos):
                    graph_visual(False)
                if random_button.checkForInput(menu_mouse_pos):
                    random_settings_graph()
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()



main_menu()