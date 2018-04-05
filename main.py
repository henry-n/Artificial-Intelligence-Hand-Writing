from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf

tf.logging.set_verbosity(tf.logging.INFO)

def CNN_classify(training_features, target_labels, mode):
	"""
	Convolutional layering classifies images. Applies convolution filters to images to produce
	a single value into the feature_training map
	
	"""

	"""
	Model function for CNN.
	"""
  
	# Input Layer
	# Reshape X/Training Image to 4-D tensor: [batch_size, width, height, channels]
	# MNIST images are 28x28 pixels, and have one color channel
	input_layer = tf.reshape(training_features["x"], [-1, 28, 28, 1])

	# Convolutional Layer #1
	# Computes 32 features using a 5x5 filter with ReLU activation.
	# Padding is added to preserve width and height.
	# Input Tensor Shape: [batch_size, 28, 28, 1]
	# Output Tensor Shape: [batch_size, 28, 28, 32]
	conv1 = tf.layers.conv2d(
		inputs=input_layer,
		filters=32,
		kernel_size=[5, 5],
		padding="same",
		activation=tf.nn.relu)

	"""
	App Logic Here
	"""
	exit("Success Preventing Loop Until Code Completes")
	
def main(arg):
	hello = tf.constant('Hello, TensorFlow!' )
	sess = tf.Session()
	print(sess.run(hello))
	print(arg)#takes itself as the file

if __name__ == '__main__': tf.app.run()#can call external function here tf.app.run(external_func)