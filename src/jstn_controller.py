from generics.controller import ImgPs4Controller
from generics.buttons import ButtonFactory
from jstn_buttons import JSTNToggleButton, JSTNJoystick, JSTNLeverButton

    
class JSTNPs4Controller(ImgPs4Controller):

  def __init__(self):
    super(JSTNPs4Controller, self).__init__(None)
    
  def create_default_factory(self):
    btnFactory = ButtonFactory()
    btnFactory.add_type("toggle", JSTNToggleButton)
    btnFactory.add_type("joystick", JSTNJoystick)
    btnFactory.add_type("lever", JSTNLeverButton)
    return btnFactory
    
  def map_buttons(self):
    # left, right, top, bottom
    self.buttons['cross'].set_coordinates(289,315,130,155)
    self.buttons['square'].set_coordinates(262,289,103,130)
    self.buttons['triangle'].set_coordinates(289,315,77,103)
    self.buttons['circle'].set_coordinates(315,342,103,130)
    
    self.buttons['L1'].set_coordinates(50, 90, 49, 53)
    self.buttons['L1'].set_color_cutoff((0, 100))
    self.buttons['R1'].set_coordinates(280, 320, 49, 53)
    self.buttons['R1'].set_color_cutoff((0, 100))
    
    self.buttons['L2'].set_coordinates(59, 86, 18, 39)
    self.buttons['L2'].set_color_range([92,92,92], [142,142,142])
    self.buttons['R2'].set_coordinates(283, 313, 18, 39)
    self.buttons['R2'].set_color_range([92,92,92], [142,142,142])
    
    self.buttons["left_joystick"].set_coordinates(95, 158, 135, 199)
    #self.buttons["right_joystick"].set_coordinates(212, 279, 135, 199)
    
