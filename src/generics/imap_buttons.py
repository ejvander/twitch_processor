from buttons import ToggleButton, Joystick
from img_map import ImgMap

class IMToggleButton(ToggleButton, ImgMap):

  def __init__(self, name):
    super(IMToggleButton, self).__init__(name)
    
  def parse_value(self, img):
    self.populate_img(img)
    self.generate_value()
    None

  def generate_value(self):
    None
    
class IMJoystick(Joystick, ImgMap):

  def __init__(self, name):
    super(IMJoystick, self).__init__(name)
    
  def set_coordinates(self, left, right, top, bottom):
    super(IMJoystick, self).set_coordinates(left, right, top, bottom)
    self.center = ((self.right-self.left)/2, (self.bottom-self.top)/2)
  
  def parse_value(self, img):
    self.populate_img(img)
    self.generate_value()
    None

  def generate_value(self):
    None