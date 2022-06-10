from screen import Screen
from player import Player
from horde import Horde

class PlayScreen(Screen):
  def __init__(self, type, game):
    super().__init__(type, game)
    self.hordes = []
    self.projectiles = []

    self.player = Player(self.game)
    self.reset()
    

  def on_click(self):
    self.game.click()

    if self.game.clicked:
      self.player.shoot()

    self.game.clicked = False


  def add_projectile(self, projectile):
    self.projectiles.append(projectile)


  def reset(self):
    player_x = (self.width - self.player.width) / 2
    player_y = self.height - self.player.height - 4
    self.player.set_position(player_x, player_y)
    self.hordes = []
    self.projectiles = []


  def render(self):
    for horde in self.hordes:
      horde.render()
      horde.move()

    for projectile in self.projectiles:
      projectile.render()
      projectile.move()

    self.check_for_hits()

    self.player.render()    


  def check_for_hits(self):
    for shot in self.projectiles:
      for horde in self.hordes:
        for line in horde.enemies:
          for enemy in line:
            if shot.collided(enemy):
              enemy.die(line)
              shot.suicide()


  def play(self):
    if len(self.hordes) != 0: return
    
    horde = Horde(self.game, 7, 4)
    self.hordes.append(horde)