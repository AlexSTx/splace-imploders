from screen import Screen

class MenuScreen(Screen):
  def __init__(self, type, game, btns = None):
    super().__init__(type, game)
    self.btns = btns
    self.set_btns_coordinates()


  def set_btns_coordinates(self):
    if not self.btns: return

    x = int((self.width - self.btns[0].width) / 2)
    distance = 20

    total_btns_height = (self.btns[0].height) * len(self.btns) + distance * (len(self.btns) - 1)
    y_thres = (self.height - total_btns_height) / 2

    for index in range(len(self.btns)):
      y = y_thres + index * (distance + self.btns[index].height)
      self.btns[index].set_coordinates(x, y)


  def on_mouse_over(self):
    if not self.btns: return

    for btn in self.btns:
      if self.game.mouse.is_over_area(btn.start_point, btn.end_point):
        if not btn.hover:
          btn.on_mouse_over()
      else:
        if btn.hover:
          btn.on_mouse_out()


  def on_click(self):
    self.game.click()

    for btn in self.btns:
      if self.game.mouse.is_over_area(btn.start_point, btn.end_point):
        if self.game.clicked:
          btn.on_click()

    self.game.clicked = False


  def render(self):
    if not self.btns: return
    for btn in self.btns:
      btn.render()
