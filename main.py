import pygame
import sys
import json

from classes import Player, Floor, Lava, Button
from utils import load_img, load_map, output, middle, import_map

pygame.init()
width = 800
height = 600
FPS = 60
clock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Template")

try:
    with open("data.json", "r") as file:
        data = json.load(file)
    name = data["name"]
    level = data["level"]
except FileNotFoundError:
    with open("data.json", "w") as file:
        json.dump({"name": "danil", "level": 1}, file)
    name = "danil"
    level = 1

# ================ MENU ================
margin = 25 # px
background = load_img("assets/back_menu.png")
buttons = pygame.sprite.Group()
senter_pos = middle(width, height, 270, 80) # Для кнопок типо rectangle размер всегда 270x80

start_button = Button("rectangle", (100, 100), "start", font_size=36, font_color=(0, 168, 120))
start_button.rect.left, start_button.rect.top = senter_pos
start_button.rect.top = start_button.rect.top - start_button.rect.height - margin

settings_button = Button("rectangle", (100, 100), "settings", font_size=36, font_color=(0, 168, 120))
settings_button.rect.left, settings_button.rect.top = senter_pos

exit_button = Button("rectangle", (100, 100), "EXIT", font_size=36, font_color=(0, 168, 120))
exit_button.rect.left, exit_button.rect.top = senter_pos
exit_button.rect.top = exit_button.rect.top + exit_button.rect.height + margin

buttons.add(start_button, settings_button, exit_button)

# ================ LEVELS ================
margin_levels_x = 100
buttons_levels = pygame.sprite.Group()
map_levels = load_map()
for key in map_levels.keys():
    buttons_levels.add(Button("rect", (margin_levels_x*key, 100), str(key)))

# ================ GAME ================
sky = load_img("assets/sky.png")
player = Player(name, f"assets/{name}.png", (100, 200), resize=(100, 220))
player.rect.bottom = 500
platform = pygame.sprite.Group()
level_map = map_levels[level]
root = False
proris_map = False

# ================ MAIN ================
game_state = "menu" #menu levels settings game
running = True

while running:
    clock.tick(FPS)

    if game_state == "menu":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in buttons:
                    if button.rect.collidepoint(event.pos):
                        if button.text == "start":
                            game_state = "levels"
                        elif button.text == "setting":
                            game_state = "setting"
                        elif button.text == "EXIT":
                            running = False
            
            screen.blit(background, (0, 0))
            buttons.draw(screen)
        
            
    elif game_state == "levels":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_state = "menu"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons_levels:
                    if button.rect.collidepoint(event.pos):
                        platform.empty()
                        proris_map = False
                        level = int(button.text)
                        level_map = map_levels[level]
                        player.rect.left = 0
                        game_state = "game"
            screen.fill((0, 0, 0))
            buttons_levels.draw(screen)

    elif game_state == "settings":
        pass #settings()
    elif game_state == "game":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_state = "levels"
                elif event.key == pygame.K_RETURN and root:
                    import_map(platform.sprites(), level)
            elif event.type == pygame.MOUSEBUTTONDOWN and root:
                x, y = event.pos
                x, y = str(x).zfill(3)[0] + "00", str(y).zfill(3)[0] + "00"

                if event.button == 1:
                    platform.add(Floor((int(x), int(y))))
                elif event.button == 2:
                    all_floors = platform.sprites()
                    first_floor = all_floors[-1]
                    platform.remove(first_floor)
                else:
                    platform.add(Lava((int(x), int(y))))

        if proris_map is False:
            floors = level_map["floor"]
            lavas = level_map["lava"] 
            for floor in floors:
                platform.add(Floor(floor))
            for lava in lavas:
                platform.add(Lava(lava))
            proris_map = True
                
        screen.blit(sky, (0, 0))
                
        if player.rect.left >= width:
            game_state = "levels"

        platform.draw(screen)
        player.update(platform)
        screen.blit(player.image, player.rect)
    
    pygame.display.flip()

