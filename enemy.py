from entity import Entity
from shot import Shot

class Enemy(Entity):
  def __init__(self, type, game, horde, difficulty = 1):
    super().__init__(f'assets/entities/enemy-{type}.png', game, 100 * difficulty)
    self.horde = horde
    self.difficulty = difficulty


  def move_side(self, direction):
    self.x += self.get_speed() * direction


  def move_down(self):
    self.y += 30


  def shoot(self):
    projectile = Shot(self.game, 2)
    projectile.set_position(self.x + self.width/2, self.y + self.height)
    projectile.set_speed(300)

    self.game.screen.add_projectile(projectile)


  def die(self, line):
    self.horde.kill(line, self)
    self.game.points += 10 * (1 + 0.5 * self.difficulty)  