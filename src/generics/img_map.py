class ImgMap(object):

  def __init__(self):
    super(ImgMap, self).__init__()
    self.left = 0
    self.right = 0
    self.top = 0
    self.bottom = 0
  
  def set_coordinates(self, left, right, top, bottom):
    self.left = left
    self.right = right
    self.top = top
    self.bottom = bottom
    
  def populate_img(self, img):
    self.img = img[self.top:self.bottom, self.left:self.right]