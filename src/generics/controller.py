from buttons import ButtonFactory

class Controller(object):
  
  def __init__(self, btnFactory):
    super(Controller, self).__init__()
    self.buttons = {}
    if(btnFactory is None):
      btnFactory = self.create_default_factory()
    self.define_buttons(btnFactory)
  
  def create_default_factory(self):
    return ButtonFactory()
  
  def define_buttons(self, btnFactory):
    Continue
    
  def __str__(self):
    out_str = ""
    for button in self.buttons:
      out_str += str(self.buttons[button]) + " "
    return out_str
    
class Ps4Controller(Controller):

  def __init__(self, btnFactory):
    super(Ps4Controller, self).__init__(btnFactory)
    
  def create_default_factory(self):
    btnFactory = ButtonFactory()
    btnFactory.add_type("toggle", ToggleButton)
    btnFactory.add_type("joystick", Joystick)
    return btnFactory
    
  def define_buttons(self, btnFactory):
    self.buttons['cross'] = btnFactory.make_button("toggle", 'cross')
    self.buttons['circle'] = btnFactory.make_button("toggle", 'circle')
    self.buttons['square'] = btnFactory.make_button("toggle", 'square')
    self.buttons['triangle'] = btnFactory.make_button("toggle", 'triangle')
    
    self.buttons['L1'] = btnFactory.make_button("toggle", 'L1')
    self.buttons['R1'] = btnFactory.make_button("toggle", 'R1')
    
    self.buttons['L2'] = btnFactory.make_button("lever", 'L2')
    self.buttons['R2'] = btnFactory.make_button("lever", 'R2')
    
    self.buttons['left_joystick'] = btnFactory.make_button("joystick", 'left_joystick')
    #self.buttons['right_joystick'] = btnFactory.make_button("joystick", 'right_joystick')
    
class ImgPs4Controller(Ps4Controller):

  def __init__(self, btnFactory):
    super(ImgPs4Controller, self).__init__(btnFactory)
    self.map_buttons()
  
  def create_default_factory(self):
    btnFactory = ButtonFactory()
    btnFactory.add_type("toggle", IMToggleButton)
    btnFactory.add_type("joystick", IMJoystick)
    return btnFactory
  
  def map_buttons(self):
    None
    
  def parse_img(self, img):
    for button in self.buttons:
      self.buttons[button].parse_value(img)
      #if(self.buttons[button].value == 1):
      #print self.buttons[button]