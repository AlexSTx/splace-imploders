from screen import Screen
from PPlay.sprite import Sprite
from os.path import exists

class ScoreScreen(Screen):
  def __init__(self, type, game):
    super().__init__(type, game)
    self.title = Sprite('assets/leaderboard.png')
    self.scores = []


  def get_scores(self):
    file_exists = exists('./data/history.txt')

    print(file_exists)

    if not file_exists:
      self.scores = []
      return

    with open('data/history.txt', encoding='utf-8') as file:
      self.scores = file.readlines()[-5:]


  def render(self):
    if self.just_entered:
      self.get_scores()
      self.just_entered = False

    x = int((self.width - self.title.width) / 2)
    
    self.title.x = x
    self.title.y = 150

    y_threshold = self.title.y + self.title.height + 32
    font_size = 32

    self.title.draw()
    for index, score in enumerate(self.scores):
      self.game.window.draw_text(score[:-1], x, y_threshold + 2*index*font_size, font_size, 'red', 'Comic-Sans')