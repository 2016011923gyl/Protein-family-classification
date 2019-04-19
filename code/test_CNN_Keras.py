#from __future__ import print_function
import keras
from keras import Model,models
from keras import backend as K
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense, Dropout, Flatten, Activation, Input
from keras.layers import Conv1D, MaxPooling1D
from keras.layers import Conv2D, MaxPooling2D
from keras.datasets import cifar10
from keras.utils import to_categorical
from keras.callbacks import Callback

from sklearn.metrics import roc_auc_score, roc_curve, auc
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import label_binarize

import itertools
import os
import numpy as np
#os.environ["CUDA_VISIBLE_DEVICES"] = "6"

batch_size = 64
num_classes = 4557
epochs = 20

# input image dimensions
img_rows, img_cols = 700, 21

x_train = np.load("../data/train_data/x_train_noSeq.npy")
y_train = np.load("../data/train_data/y_train_noSeq.npy")
x_test = np.load("../data/test_data/x_test_noSeq.npy")
y_test = np.load("../data/test_data/y_test_noSeq.npy")
print(y_train)
print(y_test)

x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
y_train = y_train.reshape(y_train.shape[0],y_train.shape[1])
y_test = y_test.reshape(y_test.shape[0],y_test.shape[1])
input_shape = (img_rows, img_cols, 1)

print('x_train shape:', x_train.shape)
print('y_train shape:', y_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# =============================================================================
# # convert class vectors to binary class matrices
# y_train = keras.utils.to_categorical(y_train, num_classes)
# y_test = keras.utils.to_categorical(y_test, num_classes)
# =============================================================================

model = Sequential()
model.add(Conv2D(64, kernel_size=(5,5),
                 activation='relu',
                 input_shape=input_shape))
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(Conv2D(32, (3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='sigmoid'))

model.compile(loss='categorical_crossentropy',
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

print("training ==========~~~~~~~~=======")
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))

print("Testing ==========~~~~~~~~~~~~======")
score = model.evaluate(x_test, y_test, verbose=0)

print('Test loss:', score[0])
print('Test accuracy:', score[1])