from PPlay.window import *
from PPlay.mouse import *
from PPlay.keyboard import *

from button import Button
from menuScreen import MenuScreen
from playScreen import PlayScreen
from gameOverScreen import GameOverScreen
from scoreScreen import ScoreScreen

class Game():
  def __init__(self):
    self.window = Window(1280, 768)
    self.keyboard = Keyboard()
    self.mouse = Mouse()
    
    self.fps = 0
    self.time = 0
    self.frame = 0

    self.screens = {}
    self.screen_label = 'main'
    self.state = {'difficulty': 1, 'last_score': 0, 'last_horde': 0}

    self.last_click = 0
    self.clickable = True
    self.clicked = True
    
    self.delay = 0.1

    self.points = 0


  def add_screen(self, screen):
    self.screens[screen.type] = screen
    # if that is the first screen being added, set the current one as that one
    if len(self.screens) == 1:
      self.change_screen(screen.type)

  
  def change_screen(self, screen_label):
    self.screen_label = screen_label
    self.screen = self.screens[screen_label]
    self.screen.just_entered = True
  

  def change_difficulty(self, difficulty):
    self.state['difficulty'] = difficulty
    print(f'difficulty: {difficulty}')


  def click(self):
    if self.clickable:
      self.clickable = False
      self.clicked = True


  def update_entry_countdown(self, delay):
    if not self.clickable:
      self.last_click += self.window.delta_time()
      if self.last_click > delay:
        self.clickable = True
        self.last_click = 0


  def exit(self):
    self.window.clear()
    self.window.delay(250)
    self.window.close()


  def count_fps(self):
    self.time += self.window.delta_time()
    self.frame += 1
    if self.time >= 1.0:
      self.fps = self.frame
      self.frame = 0
      self.time = 0


  def show_fps(self):
    self.window.draw_text(f'{self.fps}', self.window.width / 2 - 10, 5, 20, (0, 255, 0))


  def init(self):
    self.window.set_title("splace")

    # setting up screens
    main_menu_btns = [Button('play', self.change_screen, 'play_screen'), 
                      Button('difficulty', self.change_screen, 'difficulty'), 
                      Button('ranking', self.change_screen, 'score_screen'), 
                      Button('exit', self.exit)]

    difficulty_menu_btns = [Button('easy', self.change_difficulty, 1), 
                            Button('medium', self.change_difficulty, 2), 
                            Button('hard', self.change_difficulty, 3)]

    main_menu = MenuScreen('main', self, main_menu_btns)
    difficulty_menu = MenuScreen('difficulty', self, difficulty_menu_btns)
    play_screen = PlayScreen('play_screen', self)
    game_over_screen = GameOverScreen('game_over_screen', self)
    score_screen = ScoreScreen('score_screen', self)

    self.add_screen(main_menu)
    self.add_screen(difficulty_menu)
    self.add_screen(play_screen)
    self.add_screen(game_over_screen)
    self.add_screen(score_screen)


  def loop(self):
    while True:
      self.window.set_background_color([255, 255, 255])

      self.screen.render()
      self.screen.run()

      self.update_entry_countdown(self.delay)

      if self.keyboard.key_pressed('ESC') and self.screen_label != 'main':
          if self.screen_label == 'play_screen':
            self.screen.reset()
          self.change_screen('main')

      self.count_fps()
      self.show_fps()
      self.window.update()


# instantiating game
game = Game()

# loading everything
game.init()

# game loop
game.loop()