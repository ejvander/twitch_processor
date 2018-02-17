class ButtonFactory(object):

  def __init__(self):
    super(ButtonFactory, self).__init__()
    self.value = 0
    self.btnTypeMap = {}
    
  def add_type(self, typeName, typeVal):
    self.btnTypeMap[typeName] = typeVal
    
  def make_button(self, btnType, name):
    return self.btnTypeMap[btnType](name)

    
class ToggleButton(object):

  def __init__(self, name):
    super(ToggleButton, self).__init__()
    self.name = name
    self.value = 0
    
  def __str__(self):
    return "%s: %d" % (self.name, self.value)
    

class Joystick(object):

  def __init__(self, name):
    super(Joystick, self).__init__()
    self.name = name
    self.value = (0,0)
    
  def __str__(self):
    return "%s: (%+f, %+f)" % (self.name, self.value[0], self.value[1])