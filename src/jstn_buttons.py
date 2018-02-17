import cv2
import numpy as np
import math

from generics.imap_buttons import IMToggleButton, IMJoystick

DEBUG = False

class JSTNToggleButton(IMToggleButton):

  pressed_color_cutoff = 50

  def __init__(self, name):
    super(JSTNToggleButton, self).__init__(name)
    
  def generate_value(self):
    blue, green, red = (self.img[0].mean(), self.img[1].mean(), self.img[2].mean())
    if(red > self.pressed_color_cutoff):
      self.value = 1
    else:
      self.value = 0
    None

class JSTNJoystick(IMJoystick):

  # Button color bounds
  # Joystick is red in the videos, so we'll filter it out
  lower_color_bound = [0,0,130]
  upper_color_bound = [100, 100, 255]
  
  # Max range appearts to be about 13.  
  # Non-moving stick moves up to 5 px, so set that as the lower
  max_offset = 13
  min_offset = 5

  def __init__(self, name):
    super(JSTNJoystick, self).__init__(name)
    
  def filter_image(self):
    lower = np.array(self.lower_color_bound, dtype = "uint8")
    upper = np.array(self.upper_color_bound, dtype = "uint8")
    
    mask = cv2.inRange(self.img, lower, upper)
    mask = cv2.medianBlur(mask,7)
    return mask
  
  def correct_offset(self, val, val2):
    sign = -1 if val < 0 else 1
    if(abs(val) > self.max_offset):
      return sign*self.max_offset
    elif((abs(val) < self.min_offset) and (abs(val2) < self.min_offset)):
      # We only want to zero out the lower values if both values are low
      return 0
    return val
  
  def normalize_value(self, in_val):
    norm_val = [0,0]
    if(abs(in_val[0]) >= self.min_offset or abs(in_val[1]) >= self.min_offset):
      norm_val[0] = self.correct_offset(in_val[0], in_val[1])
      norm_val[1] = self.correct_offset(in_val[1], in_val[0])
    
    return (norm_val[0]/float(self.max_offset), norm_val[1]/float(self.max_offset))
  
  def generate_value(self):
    gimg = self.filter_image()
    
    circles = cv2.HoughCircles(gimg,cv2.HOUGH_GRADIENT,1,200,
                            param1=24,param2=10,minRadius=0,maxRadius=0)
    
    if(circles is not None):
      circles = np.uint16(np.around(circles))
      for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(self.img,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        if(DEBUG):
          print "circle_center: %d, %d, joystick_center: %d, %d joystick: %d %d" \
            %(i[0],i[1], self.center[0], self.center[1], i[0] - self.center[0], self.center[1]-i[1])
          
        self.value = self.normalize_value(((i[0] - self.center[0]), (self.center[1]-i[1])))
        cv2.arrowedLine(self.img, (i[0], i[1]), (self.center[0], self.center[1]), (0,0,255),2)

      cv2.imshow('detected circles',self.img)
      #cv2.imshow('image', self.img)
      cv2.waitKey(1)
      #cv2.destroyAllWindows()
    else:
      self.value = (0,0)