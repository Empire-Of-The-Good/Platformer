import pygame
import json

def load_map(file_name="level_data.json"):
    clear_map = {}
    try:
        with open(file_name, "r") as file:
            level_map = json.load(file)
    except FileNotFoundError:
        clear_map = {1: {"floor": [[0,500], [100,500], [200,500], [300,500], [400,500], [500,500], [600,500], [700,500]], "lava": [[400,500]]}}
    else:
        for key, value in level_map.items():
            clear_map[int(key)] = value
    return clear_map
        

def import_map(sprites, level, file_name="level_data.json"):
    """
    Сохраняет отредактированную карту под номер level
    """
    level_map = load_map()
    level_map[level] = {"floor":[], "lava":[]}
    for block in sprites:
        if block.type_block == "floor":
            level_map[level]["floor"].append(block.rect.topleft)
        elif block.type_block == "lava":
            level_map[level]["lava"].append(block.rect.topleft)
    with open(file_name, "w") as file:
        json.dump(level_map, file)

def load_img(img_path: str, resize: tuple[int, int] | None = None):
    img = pygame.image.load(img_path).convert_alpha()
    if resize is not None:
        img = pygame.transform.scale(img, resize)
    return img

def middle(width, height, width2, height2):
    return (width//2-width2//2, height//2-height2//2)

def get_img_text(text, font_color=(255, 0, 0), font_antialias=True, font_text=None, font_size=36):
    font = pygame.font.Font(font_text, font_size)
    text_surface = font.render(text, font_antialias, font_color)
    return text_surface

def output(screen, text, x, y, font_color=(255, 0, 0), font_antialias=True, font_text=None, font_size=36, width=800, height=600):
    text_surface = get_img_text(text, font_color, font_antialias, font_text, font_size)
    if x == "senter":
        x = width // 2 - text_surface.get_width() // 2
    if y == "senter":
        y = height//2-text_surface.get_height // 2
    screen.blit(text_surface, (x, y))