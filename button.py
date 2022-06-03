from PPlay.sprite import *

class Button():
  def __init__(self, label, action = None, action_args = None):
    self.label = label
    self.__btn_sprites = [Sprite(f"assets/buttons/btn-{self.label}-0.jpg"), Sprite(f"assets/buttons/btn-{self.label}-1.jpg")]
    self.btn = self.__btn_sprites[0]
    self.width = self.btn.width
    self.height = self.btn.height
    self.hover = False
    self.action = action
    self.action_args = action_args
    

  def on_mouse_over(self):
    self.hover = True
    self.btn = self.__btn_sprites[1]

  
  def on_mouse_out(self):
    self.hover = False
    self.btn = self.__btn_sprites[0]


  def on_click(self):
    if self.action:
      self.action(self.action_args) 


  def set_coordinates(self, x, y):
    for sprite in self.__btn_sprites:
      sprite.x = x
      sprite.y = y

    self.x = x
    self.y = y

    self.start_point = [x, y]
    self.end_point = [x + self.width, y + self.height]


  def render(self):
    self.btn.draw()