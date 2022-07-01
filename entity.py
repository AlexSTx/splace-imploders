from PPlay.sprite import Sprite

class Entity(Sprite):
  def __init__(self, sprite, game, frames = 1):
    super().__init__(sprite, frames)
    self.game = game  


  def set_position(self, x, y):
    self.x = x
    self.y = y


  def render(self):
    self.draw()