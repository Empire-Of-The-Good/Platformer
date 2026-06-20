import pygame
from utils import load_img, get_img_text, middle

class Button(pygame.sprite.Sprite):
    def __init__(self, type_button, pos, text, font_color=(255, 0, 0), font_antialias=True, font_text=None, font_size=36):
        super().__init__()
        
        self.image = load_img(f"assets/{type_button}.png")
        self.rect = pygame.Rect(*pos, *self.image.get_size())

        self.text = text
        self.text_image = get_img_text(self.text, font_color, font_antialias, font_text, font_size)
        self.text_pos = middle(*self.rect.size, *self.text_image.get_size())

        self.image.blit(self.text_image, self.text_pos)

class Block(pygame.sprite.Sprite):
    def __init__(self, pos, type_block):
        super().__init__()
        self.type_block = type_block
        self.image = load_img(f"assets/{type_block}.png")
        self.rect = pygame.Rect(*pos, *self.image.get_size())

class Floor(Block):
    def __init__(self, pos):
        super().__init__(pos, "floor")

class Lava(Block):
    def __init__(self, pos):
        super().__init__(pos, "lava")
        

class Player(pygame.sprite.Sprite):
    def __init__(self, name, path_to_img, pos, resize=(48, 96)):
        super().__init__()
        self.name = name
        self.left_sprite = load_img(path_to_img, resize)
        self.right_sprite = pygame.transform.flip(self.left_sprite, True, False)
        self.image = self.left_sprite
        self.rect = pygame.Rect(*pos, *self.image.get_size())
        self.speed_x = 6
        self.velocity_x = 0 # текущая скорость по оси X
        self.velocity_y = 0 # текущая скорость по оси Y
        self.gravity = 1
        self.jump_power = -14
        self.can_jump = True

    def reset(self):
        self.rect.left = 0
        self.rect.bottom = 100

    def hits_lava(self, lava):
        if pygame.sprite.spritecollide(self, lava, False):
            return True
        return False

    def update(self, platform): 
        floor = pygame.sprite.Group()
        lava = pygame.sprite.Group()

        for block in platform:
            if block.type_block == "floor":
                floor.add(block)
            else:
                lava.add(block)
        
        keys = pygame.key.get_pressed()

        self.velocity_x = 0
      
        if keys[pygame.K_d]:
            self.image = self.right_sprite
            self.velocity_x = self.speed_x

        if keys[pygame.K_a]:
            self.image = self.left_sprite
            self.velocity_x = -self.speed_x
        
        self.rect.left += self.velocity_x


        if self.hits_lava(lava):
            self.reset()
            return
        
        hits_x_floor = pygame.sprite.spritecollide(self, floor, False)

        for block in hits_x_floor:
            if block.rect.top >= self.rect.bottom - self.gravity:
                continue
            elif self.velocity_x > 0:
                self.rect.right = block.rect.left
            elif self.velocity_x < 0:
                self.rect.left = block.rect.right
        
        # РАБОТА С ОСЬЮ Y
        if keys[pygame.K_w] and self.can_jump:
            self.velocity_y = self.jump_power

        self.velocity_y += self.gravity
        self.rect.bottom += self.velocity_y

        if self.hits_lava(lava):
            self.reset()
            return

        self.can_jump = False
        hits_y_floor = pygame.sprite.spritecollide(self, floor, False)

        for block in hits_y_floor:
            if self.velocity_y > 0:
                self.rect.bottom = block.rect.top
                self.velocity_y = 0
                self.can_jump = True
            elif self.velocity_y < 0:
                self.rect.top = block.rect.bottom
                self.velocity_y = 0