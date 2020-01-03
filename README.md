
# Bounding Box Regression

The project demonstrates the working of the Bounding Box Regression technique used in 
object detection tasks. It can efficiently predict the four coordinates of a 
bounding box around the image. Class probabilities ignored due to the fact the dataset only includes human object.

The following files are included in this repo:

1. `DataProcessor.py` : Extract the images and XML annotations in `\images` to convert them `.npy` files
 ready for training/testing in `\processed_data`.
 
2. `Model.py` : Defines the CNN model and other useful methods.

3. `MainFile.py` : Trains the model on the data.

4. `Evaluation.py` : Loads a model from the given `h5py` file and predicts bounding 
boxes for various images, draws them on the image and then finally saves the images 
to a directory.

5. `Predict.py` : Test runs the model on the image in `\test_data` and outputs in `\test_inference_images`.

6. `Convert.py` : Convert given `h5py` file to tflite format.
