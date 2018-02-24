import cv2
import sys
import numpy as np

from keras.optimizers import Adam
from src.jstn_controller import JSTNPs4Controller
from network import JSTNNetwork

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

network = JSTNNetwork()
model = network.make_network((1080, 1920, 3), 10)
model.compile(optimizer=Adam(), loss='mean_absolute_error', metrics=['accuracy'])


#for layer in model.layers:
#  print layer.name
#  print layer.input_shape
#  print layer.output_shape

in_imgs = []
cont_vals = []

while success:
  success, image = vidcap.read()
  count += 1
  #if(count % 60 == 0):
  #  print "Processed %d seconds" % (count/60)
    
  controller_img = image[CONTROLLER_TOP:CONTROLLER_BOTTOM, CONTROLLER_LEFT:CONTROLLER_RIGHT]
  controller.parse_img(controller_img)
  
  value_arr = controller.get_value_arr()
  out_val = []
  for value in value_arr:
    try:
      out_val.extend(value)
    except:
      out_val.append(value)
  
  in_imgs.append(image)
  cont_vals.append(out_val)
  if(len(in_imgs) == 10):
    nn_images = np.array(in_imgs)
    output_val = np.array(cont_vals)
    model.fit(nn_images, output_val, epochs=1, batch_size=1)
    in_imgs = []
    cont_vals = []
  
    in_val = np.expand_dims(image, axis=0)
    preds = model.predict(in_val)
    str_format = "%+5f, %+5f, %+5f, %+5f, %+5f, %+5f, %+5f, %+5f, %+5f, %+5f"
    print ("Real Vals: " + str_format) % tuple(out_val)
    print ("Pred Vals: " + str_format) % tuple(preds[0].tolist())
  #sys.stdout.write("\r" + str(preds))
  #sys.stdout.flush()
  #out_val = np.array(out_val)
  #out_val = np.expand_dims(out_val, axis=0)
  #in_val = np.expand_dims(image, axis=0)
  #model.fit(in_val, out_val, epochs=1, batch_size=1)
  
  # Overwrite current line to keep console clean
  #sys.stdout.write("\r" + str(controller))
  #sys.stdout.flush()
  