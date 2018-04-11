from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf

"""
App Logic Here
"""
def main(arg):
	hello = tf.constant('Hello, TensorFlow!' )
	sess = tf.Session()
	print(sess.run(hello))
	print(arg)#takes itself as the file

if __name__ == '__main__': tf.app.run()#can call external function here tf.app.run(external_func)