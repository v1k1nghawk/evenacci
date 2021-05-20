#!/usr/bin/env python3
########################################################################################################################
# Purpose: produce Machine Learning model for even Fibonacci numbers
# Programmer: Andrew Art
########################################################################################################################


from fibonacci import fibonacci
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers


class FibonacciModel(tf.keras.Model):
    def __init__(self):
      '''MLP-type NN for predicting even Fibonacci numbers based on their indices.

      '''
      super(FibonacciModel, self).__init__()
      self.hidden_layer1 = tf.keras.layers.Dense(256, activation=tf.nn.relu)
      self.hidden_layer2 = tf.keras.layers.Dense(64, activation=tf.nn.tanh)
      self.hidden_layer3 = tf.keras.layers.Dense(32, activation=tf.nn.softplus)
      self.hidden_layer4 = tf.keras.layers.Dense(128, activation=tf.nn.sigmoid)
      self.output_layer = tf.keras.layers.Dense(1)

    def call(self, inputs):
      '''Transformation from inputs to outputs.

      :param inputs: input tensor(s)

      :returns: output tensor or list of output tensors
      '''
      x = self.hidden_layer1(inputs)
      x = self.hidden_layer2(x)
      x = self.hidden_layer3(x)
      x = self.hidden_layer4(x)
      return self.output_layer(x)


def produce_model() -> None:
    '''Building a Deep learning model for (index -> even Fibonacci number) predictions.

    '''
    #######
    # Dataset
    #######
    full_fib_series = np.array(fibonacci(end=1000))
    even_fib_series = np.array(full_fib_series[full_fib_series % 2 == 0], dtype=np.float64)

    DATASET_SIZE = 10000
    # Output variable - even Fibonacci number
    y_values = np.random.choice(even_fib_series, DATASET_SIZE)

    # Input variable - index of y
    x_values = np.empty(DATASET_SIZE, dtype=int)
    for i in range(DATASET_SIZE):
        x_values[i] = np.argwhere(even_fib_series == y_values[i])[0]

    # Split dataset
    TRAIN_SUBSET_SIZE = int(0.6 * DATASET_SIZE)
    TEST_SUBSET_SIZE = int(0.2 * DATASET_SIZE + TRAIN_SUBSET_SIZE)

    x_train, x_validation, x_test = np.split(x_values, [TRAIN_SUBSET_SIZE, TEST_SUBSET_SIZE])
    y_train, y_validation, y_test = np.split(y_values, [TRAIN_SUBSET_SIZE, TEST_SUBSET_SIZE])

    #######
    # Model
    #######
    fmodel = FibonacciModel()

    fmodel.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])

    training_results = fmodel.fit(x_train, y_train, validation_data=(x_validation, y_validation), epochs=20, batch_size=8, verbose=2, shuffle=True)
    print('TRAIN {mae: %.2f}, {loss: %.2f}'
          % (training_results.history['mae'][-1]*100, training_results.history['loss'][-1]))
    print('VALID {mae: %.2f}, {loss: %.2f}\n'
          % (training_results.history['val_mae'][-1]*100, training_results.history['val_loss'][-1]))

    test_results = fmodel.evaluate(x_test, y_test)
    print("TEST {%s: %.2f}, {loss: %.2f}\n" % (fmodel.metrics_names[1], test_results[1]*100, test_results[0]))

    fmodel.summary()

    try:
        fmodel.save("fibmodel")
    except IOError as e:
        print("IOError: ", str(e))


produce_model()
