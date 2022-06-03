from enemy import Enemy

class Horde():
  def __init__(self, game, lines = 0, columns = 0):
    self.game = game
    self.enemies = []
    self.enemies_on_screen = False
    self.direction = 'right'
    self.spawn(lines, columns)
    

  def spawn(self, lines, columns):
    self.enemies_on_screen = True
    for x in range(lines):
      line = []
      for y in range(columns):
        enemy = Enemy(1, self.game, self, self.game.difficulty)
        enemy.set_position(x * (enemy.width + (enemy.width / 2)), y * (enemy.height + (enemy.height / 2)))
        line.append(enemy)

      self.enemies.append(line)


  def move(self):
    min_x = self.game.screen.width
    max_x = 0
    changing_direction = False

    for line in self.enemies:
        if line[0].x < min_x:
          min_x = line[0].x
        if line[len(line) - 1].x + self.game.screen.width > max_x:
          max_x = line[len(line) - 1].x + line[len(line) - 1].width

    for line in self.enemies:
      for enemy in line: 
        if self.direction == 'right':
          if max_x + enemy.get_speed() <= self.game.screen.width:
            enemy.move_right()
          else:
            self.direction = 'left'
            changing_direction = True
            
        else:
          if min_x - enemy.get_speed() > 0:
            enemy.move_left()
          else:
            self.direction = 'right'
            changing_direction = True

        if changing_direction:
          enemy.move_down()     


  def kill(self, target):
    self.enemies.remove(target)


  def render(self):
    for line in self.enemies:
      for enemy in line:
        enemy.render()
