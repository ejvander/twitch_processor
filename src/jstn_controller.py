from generics.controller import ImgPs4Controller
from generics.buttons import ButtonFactory
from jstn_buttons import JSTNToggleButton, JSTNJoystick

    
class JSTNPs4Controller(ImgPs4Controller):

  def __init__(self):
    super(JSTNPs4Controller, self).__init__(None)
    
  def create_default_factory(self):
    btnFactory = ButtonFactory()
    btnFactory.add_type("toggle", JSTNToggleButton)
    btnFactory.add_type("joystick", JSTNJoystick)
    return btnFactory
    
  def map_buttons(self):
    self.buttons['cross'].set_coordinates(289,315,130,155)
    self.buttons['square'].set_coordinates(262,289,103,130)
    self.buttons['triangle'].set_coordinates(289,315,77,103)
    self.buttons['circle'].set_coordinates(315,342,103,130)
    
    self.buttons["left_joystick"].set_coordinates(95, 158, 135, 199)
    #self.buttons["right_joystick"].set_coordinates(212, 279, 135, 199)
    
