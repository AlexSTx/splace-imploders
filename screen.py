from abc import abstractmethod

class Screen:
  def __init__(self, type, game):
    self.type = type
    self.game = game

    self.width = game.window.width
    self.height = game.window.height


  def on_click(self):
    return None


  def on_mouse_over(self):
    return None


  @abstractmethod
  def render():
    return None