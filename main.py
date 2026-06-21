import pygame
import utils
import classes

pygame.init()
width, height = 832, 640

class GameState:
    def __init__(self, game_self):
        self.game_self = game_self
        self.next_state = None
    
    def handle_event(self, event): pass
    def update(self): pass
    def draw(self, screen): pass

class Menu(GameState):
    def __init__(self, game_self):
        super().__init__(game_self)
        self.margin = 25
        self.background = utils.load_img("assets/back_menu.png")
        self.buttons = pygame.sprite.Group()
        senter_pos = utils.middle(width, height, 270, 80) # Для кнопок типо rectangle размер всегда 270x80

        self.start_button = classes.Button("rectangle", (100, 100), "start", font_size=36, font_color=(0, 168, 120))
        self.start_button.rect.left, self.start_button.rect.top = senter_pos
        self.start_button.rect.top = self.start_button.rect.top - self.start_button.rect.height - self.margin
 
        self.settings_button = classes.Button("rectangle", (100, 100), "settings", font_size=36, font_color=(0, 168, 120))
        self.settings_button.rect.left, self.settings_button.rect.top = senter_pos

        self.exit_button = classes.Button("rectangle", (100, 100), "EXIT", font_size=36, font_color=(0, 168, 120))
        self.exit_button.rect.left, self.exit_button.rect.top = senter_pos
        self.exit_button.rect.top = self.exit_button.rect.top + self.exit_button.rect.height + self.margin

        self.buttons.add(self.start_button, self.settings_button, self.exit_button)
 
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for button in self.buttons:
                if button.rect.collidepoint(event.pos):
                    if button.text == "start":
                        self.next_state = "levels"
                    elif button.text == "settings":
                        self.next_state = "settings"
                    elif button.text == "EXIT":
                        self.game_self.running = False # Тушим главный цикл напрямую!
    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        self.buttons.draw(screen)

class LevelsMenu(GameState):
    def draw(self, screen):
        screen.fill((50, 80, 50))

class Gameplay(GameState):
    def draw(self, screen):
        screen.fill((50, 80, 50))

class SettingsMenu(GameState):
    def draw(self, screen):
        screen.fill((80, 50, 80))

class ShopMenu(GameState):
    def draw(self, screen):
        screen.fill((80, 80, 50))

class Game:
    def __init__(self, width, height, FPS, caption):
        self.width = width
        self.height = height
        self.caption = caption
        self.FPS = FPS

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.caption)

        self.states = {
            "menu": Menu(self),
            "levels": LevelsMenu(self),
            "shop": ShopMenu(self),
            "settings": SettingsMenu(self),        
            "game":  Gameplay(self),
        }
        self.current_state = self.states["menu"]
        self.running = True
    
    def change_state(self):
        if self.current_state.next_state is not None:
            next_state_name = self.current_state.next_state
            self.current_state.next_state = None
            self.current_state = self.states[next_state_name]
    
    def run(self):
        while self.running:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.current_state.handle_event(event)
            
            self.current_state.update()
            self.change_state()
            self.current_state.draw(self.screen)
           
            pygame.display.flip()
        pygame.quit()

if __name__ == "__main__":
    game = Game(width=width, height=height, FPS=60, caption="My Platformer")
    game.run()
