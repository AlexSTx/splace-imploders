from screen import Screen
from PPlay.sprite import Sprite

class GameOverScreen(Screen):
  def __init__(self, type, game):
    super().__init__(type, game)
    self.title = Sprite('assets/game-over.png')

    # this delay is to avoid asking in the console before the window is updated after the render method is executed
    self.delay = 2


  def reset_delay(self):
    self.delay = 2


  def run(self):
    if self.delay <= 0:
      name = input("name: ")
      score = self.game.state['last_score']
      line = f'{name} {score}\n'

      with open('data/history.txt', 'a', encoding = 'utf-8') as file:
        file.write(line)
        self.game.change_screen('main')


  def render(self):
    x = int((self.width - self.title.width) / 2)
    
    self.title.x = x
    self.title.y = 200

    hordes_survived = self.game.state['last_horde'] - 1
    score = self.game.state['last_score']

    y_threshold = self.title.y + self.title.height + 32
    font_size = 24

    self.title.draw()
    self.game.window.draw_text(f'{score} POINTS', x, y_threshold + font_size, font_size)
    self.game.window.draw_text(f'{hordes_survived} HORDES SURVIVED', x, y_threshold + 3*font_size, font_size)
    self.game.window.draw_text('write ur name in the console pls', x, y_threshold + 6*font_size, font_size)

    self.delay -= 1
