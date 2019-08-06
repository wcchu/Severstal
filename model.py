# -*- coding: utf-8 -*-
"""

"""

# import numpy as np
# import pandas as pd
# from optparse import OptionParser
import logging
import tensorflow as tf


# TensorFlow model
class Model(tf.Module):

    def __init__(self):
        self.c0 = tf.constant(0.0, dtype=tf.float32)
        self.c1 = tf.constant(1.0, dtype=tf.float32)

    @tf.function(input_signature=[tf.TensorSpec(shape=[], dtype=tf.float32)])
    def __call__(self, x):
        y = self.c0 + self.c1 * x
        return y


def run():
    """run"""

    # create model instance
    model = Model()

    # save model
    tf.saved_model.save(model, export_dir='saved_model')


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.WARNING)
    run()
