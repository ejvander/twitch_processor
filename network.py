from keras.models import Model
from keras.layers import Dense, Activation, Input, Flatten
from keras.layers import Conv2D, MaxPooling2D, AveragePooling2D
from keras.layers.core import Reshape
from keras.layers.normalization import BatchNormalization

class JSTNNetwork(object):

  def make_network(self, inp_shape, num_classes):
    main_input = Input(shape=inp_shape, name="main_input")
    
    x = Conv2D(64, (7, 7), strides=(2, 2), padding='same')(main_input)
    x = BatchNormalization(axis=1)(x)
    x = Activation('relu')(x)
    
    x = MaxPooling2D(pool_size=(4, 4), strides=(3, 3))(x)
    
    x = Conv2D(128, (3, 3), padding='same')(x)
    x = BatchNormalization(axis=1)(x)
    x = Activation('relu')(x)
    
    x = MaxPooling2D(pool_size=(4, 4), strides=(3, 3))(x)
    x = MaxPooling2D(pool_size=(4, 4), strides=(3, 3))(x)
    
    x = Flatten()(x)
    x = Dense(num_classes, activation='linear')(x)
    main_output = Reshape((num_classes,))(x)
    
    model = Model(input=main_input, output=main_output)
    
    return model