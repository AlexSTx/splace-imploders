from entity import Entity

class Shot(Entity):
  def __init__(self, game, type = 1):
    super().__init__(f'assets/entities/shot-{type}.png', game)
    self.type = type


  def move(self):
    if self.type == 1:
      self.y -= self.get_speed()

    if self.y < self.height * -1:
      self.suicide()


  def suicide(self):
    self.game.screen.projectiles.remove(self)