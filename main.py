import tensorflow as tf 
import cv2


print("CV2 version:", cv2.__version__)
print("Tensorflow version:", tf.__version__)

print(tf.test.is_built_with_cuda())
print("--------------------")
print(tf.config.list_physical_devices('GPU'))



import os
import sys

print(os.path.dirname(sys.executable))