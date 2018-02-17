import cv2
import sys
from src.jstn_controller import JSTNPs4Controller

CONTROLLER_LEFT = 1320
CONTROLLER_RIGHT = 1692
CONTROLLER_TOP = 880
CONTROLLER_BOTTOM = 1080

START_TIME = 12000

vidcap = cv2.VideoCapture("twitch.mp4")
vidcap.set(cv2.CAP_PROP_POS_FRAMES, START_TIME)
success, image = vidcap.read()

print "%f fps video" % (vidcap.get(cv2.CAP_PROP_FPS))

# Initialize count to start time
count = START_TIME
success = True
controller = JSTNPs4Controller()
while success:
  success, image = vidcap.read()
  count += 1
  #if(count % 60 == 0):
  #  print "Processed %d seconds" % (count/60)
    
  controller_img = image[CONTROLLER_TOP:CONTROLLER_BOTTOM, CONTROLLER_LEFT:CONTROLLER_RIGHT]
  controller.parse_img(controller_img)
  
  # Overwrite current line to keep console clean
  sys.stdout.write("\r" + str(controller))
  sys.stdout.flush()
  