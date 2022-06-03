from entity import Entity
from shot import Shot

class Player(Entity):
  def __init__(self, game):
    super().__init__('assets/entities/player.png', game, 400)


  def move_left(self):
    if self.x - self.get_speed() >= 0:
      self.x -= self.get_speed()
    else:
      self.x = 0


  def move_right(self):
    if self.x + self.width + self.get_speed() <= self.game.screen.width: 
      self.x += self.get_speed()
    else:
      self.x = self.game.screen.width - self.width


  def shoot(self):
    projectile = Shot(self.game)
    projectile.set_position(self.x + self.width / 2, self.y)
    projectile.set_speed(200)

    self.game.screen.add_projectile(projectile)
