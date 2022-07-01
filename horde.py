from random import random
from enemy import Enemy

class Horde():
  def __init__(self, game, lines = 0, columns = 0):
    self.game = game
    self.enemies = []
    self.horde_size = 0
    self.enemies_on_screen = 0
    self.direction = 1
    self.speed = self.game.difficulty * 50
    self.spawn(lines, columns)
    self.bounds = ((0, 0), (0, 0))

    self.last_attack = 0
    self.delay_threshold = 0.9 / (2 * self.game.difficulty)
    self.attack_delay = self.delay_threshold
    

  def spawn(self, lines, columns):
    self.horde_size = lines * columns
    self.enemies_on_screen = self.horde_size

    for x in range(lines):
      line = []
      for y in range(columns):
        enemy = Enemy(1, self.game, self, self.game.difficulty)
        enemy.set_position(y * (enemy.width + (enemy.width / 2)), x * (enemy.height + (enemy.height / 2)))
        line.append(enemy)

      self.enemies.append(line)
    
    self.update_bounds()


  def set_speed(self, speed):
    self.speed = speed


  def get_speed(self):
    return self.speed * self.game.window.delta_time()


  def update_bounds(self):
    min_x = self.game.screen.width
    max_x = 0

    for line in self.enemies:
        if len(line) == 0:
          self.enemies.remove(line)
        else:
          if line[0].x < min_x:
            min_x = line[0].x
            
          # TODO: A RAIZ DO PROBLEMA TÁ AQUI!! A RAIZ DE TODO O MALLLLL
          x = line[len(line) - 1].x + line[len(line) - 1].width
          if x > max_x: max_x = x

    if len(self.enemies) > 0:
      min_y = self.enemies[0][0].y
      max_y = self.enemies[len(self.enemies) - 1][0].y + self.enemies[len(self.enemies) - 1][0].height
      self.bounds = ((min_x, min_y), (max_x, max_y))
    else:
      self.bounds = ((0, 0), (0, 0))


  def move(self):
    changing_direction = False

    if (self.bounds[1][0] + self.get_speed() <= self.game.screen.width and self.direction > 0) or (self.bounds[0][0] - self.get_speed() > 0 and self.direction < 0):
      for line in self.enemies:
        for enemy in line: 
          enemy.move_side(self.direction, self.get_speed())
    else:
      self.direction *= -1
      changing_direction = True

    if changing_direction:
      for line in self.enemies:
        for enemy in line: 
          enemy.move_down()     

    self.update_bounds()



  def __choose_enemy(self):
    line = round(random() * (len(self.enemies)-1))
    enemy = round(random() * (len(self.enemies[line])-1))
    return line, enemy


  def __can_attack(self):
    if self.last_attack <= 0:
      return True
    else:
      self.last_attack -= self.game.window.delta_time()
      return False


  def act(self):    
    if self.enemies_on_screen != 0:
      if self.__can_attack():
        line, enemy = self.__choose_enemy()
        self.enemies[line][enemy].shoot()
        self.attack_delay = self.delay_threshold * (random() + 1)
        self.last_attack = self.attack_delay


  def kill(self, line, target):
    self.enemies[line].remove(target)
    self.enemies_on_screen -= 1


  def render(self):
    for line in self.enemies:
      for enemy in line:
        enemy.render()
