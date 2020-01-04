import tensorflow as tf

from Model import ObjectLocalizer
from tensorflow import keras

input_shape = (32,32,1)
alpha = 0.2

# Create model backbone (make sure updated according to Model.py)
model_layers = [
    keras.layers.Conv2D(4, kernel_size=(3, 3), strides=1,
                        input_shape=input_shape),
    keras.layers.LeakyReLU(alpha=alpha),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),

    keras.layers.Conv2D(4, kernel_size=(3, 3), strides=1),
    keras.layers.LeakyReLU(alpha=alpha),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),

    keras.layers.Flatten(),

    keras.layers.Dense(5),
    keras.layers.LeakyReLU(alpha=alpha),

    keras.layers.Dense(5),
    keras.layers.LeakyReLU(alpha=alpha)
]

model = keras.Sequential(model_layers)

# Load keras model
model.load_weights('models/model.h5')
model.save('convert/model_no_opt.h5', include_optimizer=False)

# Convert the model.
converter = tf.lite.TFLiteConverter.from_keras_model_file('convert/model_no_opt.h5')
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()
open("convert/converted_model.tflite", "wb").write(tflite_model)
