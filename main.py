import pygame
import sys
import random
import time
from text import *

pygame.init()

display_info = pygame.display.Info()
width, height = display_info.current_w, display_info.current_h
# width, height = 1000, 1000
FPS = 60
clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
gray = (200, 200, 200)
orange = (255, 165, 0)
light_blue = (173, 116, 233)


screen = pygame.display.set_mode((width, height))
screen_color = black
pygame.display.set_caption('Chop Down Tree')
font = pygame.font.Font(None, 36)



def tutorial_screen():
  tui = True
  
  
  while tui:
    screen.fill(black)
    
    
    
    home = pygame.Rect(width // 2 - 200, height - 150, 400, 100)
    mouse_pos = pygame.mouse.get_pos()
    if home.collidepoint(mouse_pos):
      write(screen, home, "Home", 65, "black", "gray69", 10)
    else:
      write(screen, home, "Home", 65, "black", "white", 10)

    pygame.display.flip()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pygame.quit()
          sys.exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if home.collidepoint(mouse_pos):
          tui = False
          start_screen()
    


def show_text_on_screen(text, font_size, y_position, color=gray, x=0):
  font_local = pygame.font.Font(None, font_size)
  text_render = font_local.render(text, True, color)
  text_rect = text_render.get_rect(center=(width // 2 + x, y_position))
  screen.blit(text_render, text_rect)

def draw(text, font_size, y_position):
  font_local = pygame.font.Font(None, font_size)
  text_render = font_local.render(text, True, gray)
  text_rect = text_render.get_rect(center=(width // 2, y_position))
  screen.blit(text_render, text_rect)

def start_screen():
  start = True
  
  btn_motion_y = 0
  btn_motion_dir = -1
  btn_max_motion = 3.5

  text_colour_change_interval = 2
  title_color = 150
  mission_color = 100
  
  reverse_title_color_dir = 1
  reverse_mission_color_dir = 1
  
  title_motion_x = 0
  mission_motion_x = 0
  title_motion_dir = -1
  title_max_motion = 5

  while start:
    screen.fill(black)
    
    btn_motion_y += 0.1 * btn_motion_dir
    
    if (btn_motion_y > btn_max_motion): 
      btn_motion_dir = -1
    elif (btn_motion_y < -btn_max_motion):
      btn_motion_dir = 1
    
    
    title_motion_x += 0.1 * title_motion_dir
    mission_motion_x += 0.1 * -title_motion_dir
    
    if (title_motion_x > title_max_motion):
      title_motion_dir = -1
    elif (title_motion_x < -title_max_motion):
      title_motion_dir = 1
    
    title_color += 0.75 * reverse_title_color_dir
    mission_color += 1 * reverse_mission_color_dir
    
    # while ((title_color % 255) < 10 or (title_color * 2) % 255 < 10 or (title_color * 3) % 255 < 10):
    #   title_color += 100
    
    if (title_color <= 100): 
      reverse_title_color_dir = 1
    elif (title_color * 1.5 >= 255):
      reverse_title_color_dir = -1
    
    if (mission_color >= 255):
      reverse_mission_color_dir = -1
    elif (mission_color <= 100):
      reverse_mission_color_dir = 1
    
    show_text_on_screen("Chop Down Elvin The Tree", 100, height // 4, (title_color, title_color * 1.5, title_color * 1.25), title_motion_x)
    # show_text_on_screen("Press spacebar to start...", 50, height // 2)
    
    show_text_on_screen("Mission: Try your best to aim for as high a score as possible", 85, height // 2 - 100, (mission_color, mission_color, mission_color), mission_motion_x)
    
    mouse_pos = pygame.mouse.get_pos()
    
    pygame.mouse.set_visible(1)
    
    start_btn = pygame.Rect(width // 2 - 200, height // 2 + 50 + btn_motion_y, 400, 100)
    
    if start_btn.collidepoint(mouse_pos):
      write(screen, start_btn, "Start", 65, "black", "gray69", 10)
    else:
      write(screen, start_btn, "Start", 65, "black", "white", 10)
    
    # show_text_on_screen("Move the platform with arrow keys...", 65, height // 1.5)
    
    tutorial = pygame.Rect(width // 2 - 200, height // 2 + 200 + btn_motion_y, 400, 100)
    
    if tutorial.collidepoint(mouse_pos):
      write(screen, tutorial, "Tutorial", 65, "black", "gray69", 10)
    else:
      write(screen, tutorial, "Tutorial", 65, "black", "white", 10)
    
    
    # show_text_on_screen("Press L for Leaderboard", 75, height // 1.2 + 80)
    
    # leaderboard = pygame.Rect(width // 2 - 200, height // 2 + 350, 400, 100)
    
    # if leaderboard.collidepoint(mouse_pos):
    #   write(screen, leaderboard, "Leaderboard", 65, "black", "gray69", 10)
    # else:
    #   write(screen, leaderboard, "Leaderboard", 65, "black", "white", 10)
    
    pygame.display.flip()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pygame.quit()
          sys.exit()
        # elif event.key == pygame.K_l:
        #   start = False
        #   leaderboard_screen()
        # elif event.key == pygame.K_r:
        #   start = False
        #   login()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        if start_btn.collidepoint(mouse_pos):
          start = False
          cntdown()
        elif tutorial.collidepoint(mouse_pos):
          start = False
          tutorial_screen()
        # elif leaderboard.collidepoint(mouse_pos):
        #   start = False
        #   leaderboard_screen()
      




def cntdown():
  screen.fill(black)
  cnt = ["3", "2", "1"]
  pygame.mouse.set_visible(0)
  for number in cnt:
    draw(number, 100, height // 2)
    pygame.display.flip()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pygame.quit()
          sys.exit()
    time.sleep(1)
    screen.fill(black)
  
  main()

# def wait_for_key():
#   waiting = True
#   while waiting:
#     for event in pygame.event.get():
#       if event.type == pygame.QUIT:
#         pygame.quit()
#         sys.exit()
#       elif event.type == pygame.KEYDOWN:
#         if event.key == pygame.K_SPACE:
#           waiting = False
#         elif event.key == pygame.K_ESCAPE:
#           pygame.quit()
#           sys.exit()
#         elif event.key == pygame.K_r:
#           waiting = False
#           login()



def main():
  

  game_running = True
  while game_running:
    screen.fill(black)
    
    
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          pygame.quit()
          sys.exit()
        elif event.key == pygame.K_LSHIFT:
          game_running = False
          start_screen()

    

    pygame.display.flip()
    clock.tick(FPS)

start_screen()
pygame.display.flip()