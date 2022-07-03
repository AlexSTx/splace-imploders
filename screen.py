from abc import abstractmethod

class Screen:
  def __init__(self, type, game):
    self.type = type
    self.game = game

    self.width = game.window.width
    self.height = game.window.height

    self.just_entered = False


  def on_click(self):
    return None


  def on_mouse_over(self):
    return None


  def run(self):
    self.on_mouse_over()

    if self.game.mouse.is_button_pressed(1):
      self.game.delay = 0.3
      self.on_click()


  @abstractmethod
  def render():
    return None