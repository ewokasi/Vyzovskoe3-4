import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf

print(tf.config.list_physical_devices('GPU'))