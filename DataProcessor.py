
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer
import xmltodict
import numpy as np
import glob
import os


image_dim = 32
rootimages_dir = 'images'
rootxml_dir = 'images/labels'
output_dir = 'processed_data'
xml_filepaths = []
img_filepaths = []

xml_filepaths.extend(glob.glob( os.path.join( rootxml_dir+'/331' , '*.xml' ) ))
img_filepaths.extend(glob.glob( os.path.join( rootimages_dir+'/331' , '*.npy' ) ))
xml_filepaths.extend(glob.glob( os.path.join( rootxml_dir+'/332' , '*.xml' ) ))
img_filepaths.extend(glob.glob( os.path.join( rootimages_dir+'/332' , '*.npy' ) ))
xml_filepaths.extend(glob.glob( os.path.join( rootxml_dir+'/333' , '*.xml' ) ))
img_filepaths.extend(glob.glob( os.path.join( rootimages_dir+'/333' , '*.npy' ) ))

images = []
for filepath in img_filepaths:
	# image = Image.open( filepath ).resize( ( image_dim , image_dim ) )
	# images.append( np.asarray( image ) / 255 )
	image = np.load(filepath)
	images.append(np.reshape(image,(image_dim,image_dim,1)))

bboxes = []
classes = []
for filepath in xml_filepaths:
	bbox_dict = xmltodict.parse( open( filepath , 'rb' ) )
	classes.append( bbox_dict[ 'annotation' ][ 'object' ][ 'name' ] )
	bndbox = bbox_dict[ 'annotation' ][ 'object' ][ 'bndbox' ]
	bounding_box = [ 0.0 ] * 4
	bounding_box[0] = int(bndbox[ 'xmin' ]) / image_dim
	bounding_box[1] = int(bndbox[ 'ymin' ]) / image_dim
	bounding_box[2] = int(bndbox[ 'xmax' ]) / image_dim
	bounding_box[3] = int(bndbox[ 'ymax' ]) / image_dim
	bboxes.append( bounding_box )

bboxes = np.array( bboxes )
classes = np.array( classes )
encoder = LabelBinarizer()
classes_onehot = encoder.fit_transform( classes )

X = images
Y = np.concatenate( [ bboxes , classes_onehot ] , axis=1 )

train_features , test_features ,train_labels, test_labels = train_test_split( X , Y , test_size=0.4 )

np.save( os.path.join( output_dir , 'x.npy' ) , train_features )
np.save( os.path.join( output_dir , 'y.npy' )  , train_labels )
np.save( os.path.join( output_dir , 'test_x.npy' ) , test_features )
np.save( os.path.join( output_dir , 'test_y.npy' ) , test_labels )