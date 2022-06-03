from PPlay.sprite import Sprite

class Entity(Sprite):
  def __init__(self, sprite, game, speed = 100):
    super().__init__(sprite)
    self.game = game  
    self.__speed = speed


  def set_position(self, x, y):
    self.x = x
    self.y = y


  def set_speed(self, speed):
    self.__speed = speed


  def get_speed(self):
    return self.__speed * self.game.window.delta_time()


  def render(self):
    self.draw()