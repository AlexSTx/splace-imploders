from entity import Entity

class Enemy(Entity):
  def __init__(self, type, game, horde, difficulty = 1):
    super().__init__(f'assets/entities/enemy-{type}.png', game, 100 * difficulty)
    self.horde = horde


  def move_right(self):
    self.x += self.get_speed()
  
  
  def move_left(self):
    self.x -= self.get_speed()


  def move_down(self):
    self.y += 30


  def die(self):
    self.horde.kill(self)
  