from random import randint
from screen import Screen
from player import Player
from horde import Horde

class PlayScreen(Screen):
  def __init__(self, type, game):
    super().__init__(type, game)
    self.horde = 0
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
    self.game.delay = 0.2 + (0.075 * self.game.state['difficulty'])

    self.player.life = 5
    self.player.set_curr_frame(0)
    self.player.mortal = True
    self.player.immortal_time = 0
    self.player.spawn()
    
    self.horde = 0
    self.hordes = []
    self.projectiles = []
    self.game.points = 0


  def update(self):
    for horde in self.hordes:
      horde.move()
      horde.act()
      if horde.bounds[1][1] > self.game.window.height:
        self.game_over()

    for projectile in self.projectiles:
      projectile.move()
      self.check_for_hits(projectile)

    if not self.player.mortal:
      self.player.update_immortal_timer()


  def check_for_hits(self, shot):
    if shot.type == 1:
      for horde in self.hordes:
        if shot.x >= horde.bounds[0][0] and shot.x <= horde.bounds[1][0] and shot.y >= horde.bounds[0][1] and shot.y <= horde.bounds[1][1]:
          for line in range(len(horde.enemies)-1, -1, -1):
            for enemy in horde.enemies[line]:
              if shot.collided(enemy):
                enemy.take_hit(line)
                shot.suicide()
                horde.update_bounds()
                if horde.enemies_on_screen == 0:
                  self.hordes = []
                return True
 

    if shot.type == 2:
      if shot.y + shot.height >= self.player.y:
        if shot.collided(self.player):
          if self.player.mortal:
            self.player.die()
            if self.player.life > 0:
              self.player.spawn()
            else:
              self.game_over()
          return True
    return False


  def game_over(self):
    self.game.state['last_horde'] = self.horde
    self.game.state['last_score'] = self.game.points
    self.reset()
    self.game.change_screen('game_over_screen')


  def show_points(self):
    self.game.window.draw_text(f'{int(self.game.points)}', 16, 16, 32, (0, 0, 0))

  
  def show_life(self):
    self.game.window.draw_text(f'{self.player.life}', self.game.window.width - 32, 16, 32, (255, 0, 0))


  def horde_control(self):
    if len(self.hordes) != 0: return
    
    vertical_amout = randint(2, 4)
    horizontal_amount = randint(4, 7)

    self.horde += 1
    horde = Horde(self.game, self.horde, vertical_amout, horizontal_amount)
    self.hordes.append(horde)


  def run(self):
    self.horde_control()
    self.update()

    if self.game.keyboard.key_pressed('LEFT') or self.game.keyboard.key_pressed('A'):
      self.player.move_left()

    if self.game.keyboard.key_pressed('RIGHT') or self.game.keyboard.key_pressed('D'):
      self.player.move_right()
  
    if self.game.keyboard.key_pressed('SPACE'):
      self.on_click()


  def render(self):
    for horde in self.hordes:
      horde.render()

    for projectile in self.projectiles:
        projectile.render()

    self.show_life()
    self.show_points()
    self.player.render()    