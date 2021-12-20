import tensorflow as tf
from tensorflow import keras

sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=True))
saver = tf.train.import_meta_graph('models/vaihingen/model-99.meta')
saver.restore(sess,tf.train.latest_checkpoint('models/vaihingen/.'))

prediction_np = sess.run(prediction,feed_dict={x:batch})