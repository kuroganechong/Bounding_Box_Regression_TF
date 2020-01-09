
from datetime import datetime

import numpy as np
from tensorflow.python.keras.callbacks import EarlyStopping, TensorBoard
from PIL import Image, ImageDraw

from Model import ObjectLocalizer

input_dim = 32

X = np.load( 'processed_data/x.npy')
Y = np.load( 'processed_data/y.npy')
test_X = np.load( 'processed_data/test_x.npy')
test_Y = np.load( 'processed_data/test_y.npy')

print( X.shape )
print( Y.shape )
print( test_X.shape )
print( test_Y.shape )

localizer = ObjectLocalizer( input_shape=( input_dim , input_dim , 1 ) )
# localizer.load_model_weights( 'models/model.h5')

print(localizer.summary())

# Instantiate Tensorboard for visualisation
logdir = ".\\logs\\" + datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = TensorBoard(log_dir=logdir)

parameters = {
    'batch_size' : 32 ,
    'epochs' : 200 ,
    'callbacks' : [tensorboard_callback] ,
    'val_data' : ( test_X , test_Y )
}

localizer.fit( X , Y  , hyperparameters=parameters )
localizer.save_model( 'models/model.h5')
