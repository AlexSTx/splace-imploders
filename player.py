from entity import Entity
from shot import Shot

class Player(Entity):
  def __init__(self, game):
    super().__init__('assets/entities/player.png', game, 400, 2)
    self.life = 3
    self.mortal = True

    self.immortal_time = 0


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


  def die(self):
    if self.mortal:
      self.life -= 1
      self.mortal = False
      self.immortal_time = 2
      self.set_curr_frame(1)
      

  def update_immortal_timer(self):
    self.immortal_time -= self.game.window.delta_time()
    if self.immortal_time <= 0:
      self.mortal = True
      self.immortal_time = 0
      self.set_curr_frame(0)


  def spawn(self):
    player_x = (self.game.window.width - self.width) / 2
    player_y = self.game.window.height - self.height - 4
    self.set_position(player_x, player_y)
