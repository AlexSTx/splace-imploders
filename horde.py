from enemy import Enemy

class Horde():
  def __init__(self, game, lines = 0, columns = 0):
    self.game = game
    self.enemies = []
    self.enemies_on_screen = False
    self.direction = 1
    self.spawn(lines, columns)
    self.bounds = ((0, 0), (0, 0))
    

  def spawn(self, lines, columns):
    self.enemies_on_screen = True
    for x in range(lines):
      line = []
      for y in range(columns):
        enemy = Enemy(1, self.game, self, self.game.difficulty)
        enemy.set_position(x * (enemy.width + (enemy.width / 2)), y * (enemy.height + (enemy.height / 2)))
        line.append(enemy)

      self.enemies.append(line)
    
    self.update_bounds()


  def update_bounds(self):
    min_x = self.game.screen.width
    max_x = 0

    for line in self.enemies:
        if len(line) == 0:
          self.enemies.remove(line)
        else:
          if line[0].x < min_x:
            min_x = line[0].x
          if line[len(line) - 1].x + self.game.screen.width > max_x:
            max_x = line[len(line) - 1].x + line[len(line) - 1].width

    if len(self.enemies) > 0:
      min_y = self.enemies[0][0].y
      max_y = self.enemies[len(self.enemies) - 1][0].y + self.enemies[len(self.enemies) - 1][0].height
      self.bounds = ((min_x, min_y), (max_x, max_y))
    else:
      self.bounds = ((0, 0), (0, 0))


  def move(self):
    changing_direction = False

    for line in self.enemies:
      for enemy in line: 
        if (self.bounds[1][0] + enemy.get_speed() <= self.game.screen.width and self.direction > 0) or (self.bounds[0][0] - enemy.get_speed() > 0 and self.direction < 0):
          enemy.move_side(self.direction)
        else:
          self.direction *= -1
          changing_direction = True

        if changing_direction:
          enemy.move_down()     
    
    self.update_bounds()


  def kill(self, line, target):
    line.remove(target)
    self.update_bounds()


  def render(self):
    for line in self.enemies:
      for enemy in line:
        enemy.render()
