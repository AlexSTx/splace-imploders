from entity import Entity

class Shot(Entity):
  def __init__(self, game, type = 1, frames = 1):
    super().__init__(f'assets/entities/shot-{type}.png', game, frames)
    self.type = type
    self.__speed = 200


  def move(self):    
    if self.type == 1:
      self.y -= self.get_speed()

      if self.y < self.height * -1:
        self.suicide()

    if self.type == 2:
      self.y += self.get_speed()

      if self.y > self.game.window.height:
        self.suicide()


  def set_speed(self, speed):
    self.__speed = speed


  def get_speed(self):
    return self.__speed * self.game.window.delta_time()


  def suicide(self):
    self.game.screen.projectiles.remove(self)