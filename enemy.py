from entity import Entity

class Enemy(Entity):
  def __init__(self, type, game, horde, difficulty = 1):
    super().__init__(f'assets/entities/enemy-{type}.png', game, 100 * difficulty)
    self.horde = horde
    self.difficulty = difficulty


  def move_side(self, direction):
    self.x += self.get_speed() * direction


  def move_down(self):
    self.y += 30


  def die(self, line):
    self.horde.kill(line, self)
    self.game.points += 10 * (1 + 0.5 * self.difficulty)  