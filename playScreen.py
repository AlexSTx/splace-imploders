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
    self.game.points = 0


  def render(self):

    for projectile in self.projectiles:
      projectile.move()
      if not self.check_for_hits(projectile):
        projectile.render()

    for horde in self.hordes:
      horde.move()
      horde.render()
      horde.update_bounds()

    self.show_points()
    self.player.render()    


  def check_for_hits(self, shot):
    for horde in self.hordes:
      if shot.x >= horde.bounds[0][0] and shot.x <= horde.bounds[1][0] and shot.y >= horde.bounds[0][1] and shot.y <= horde.bounds[1][1]:
        for line in range(len(horde.enemies)-1, -1, -1):
          for enemy in horde.enemies[line]:
            if shot.collided(enemy):
              enemy.die(line)
              shot.suicide()
              horde.update_bounds()
              return True
    return False

  def show_points(self):
    self.game.window.draw_text(f'{int(self.game.points)}', 16, 16, 32, (0, 0, 0))


  def play(self):
    if len(self.hordes) != 0: return
    
    horde = Horde(self.game, 4, 7)
    self.hordes.append(horde)