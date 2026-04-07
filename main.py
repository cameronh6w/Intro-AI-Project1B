#  python3 -u "/Users/cameroncianciolo/Documents/GitHub/Intro-AI-Project1B/main.py"

# code from youtuber BaralTech video "HOW TO MAKE A MENU SCREEN IN PYGAME!"
import pygame, sys
from button import Button
import graphing
import networkx as nx
import random
import drawing

pygame.init()

seed = 8


screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def results():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        screen.fill("white")

        #title
        r_title_text = get_font(50).render("Results", True, "#b68f40")
        r_title_rect = r_title_text.get_rect(center=(640, 100))
        screen.blit(r_title_text, r_title_rect)

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
                    main_menu()
        pygame.display.update()

def graph_visual(is_random):
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



        #-------------------------
        if(is_random):
            random.seed(seed)
            drawing.draw_random_graph(screen)
        else:
            drawing.draw_preset_graph(screen)


        #-------------------------
         
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

        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if v_back_button.checkForInput(v_mouse_pos):
                    main_menu()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if v_next_button.checkForInput(v_mouse_pos):
                    results()

        pygame.display.update()

def random_settings_graph():
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

        e_weight_text = get_font(20).render("Edge Weight Distribution: ", True, "#b68f40")
        e_weight_rect = e_weight_text.get_rect(center=(435, 330))
        screen.blit(e_weight_text, e_weight_rect)
       
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
                if seed_button.checkForInput(r_mouse_pos):
                    global seed
                    seed = random.randint(1, 10)

        pygame.display.update()

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