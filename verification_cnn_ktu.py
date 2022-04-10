from numpy import loadtxt
import numpy
from keras.models import load_model
from sklearn.metrics import confusion_matrix
from numpy import savetxt
import tensorflow
from numpy import mean
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import minmax_scale
from numpy.random import seed
from tensorflow.random import set_seed


# setting the seed
seed(1)
set_seed(1)

rScaler = RobustScaler(with_centering=True, with_scaling=True, quantile_range=(20, 100-20), unit_variance=True)

# load the test data
X = loadtxt('/content/EEGData_512_44_Samples_ktu.csv', delimiter=',')

input = rScaler.fit_transform(X[:, 0:1740])
#input = X[:, 0:1740]

# transform the data in the format which the model wants
input = input.reshape(len(input), 30, 58)

# get the expected outcome 
y_real = X[:, -1]

# load the model
model = load_model('/content/best_model.h5')

# get the "predicted class" outcome
y_hat = model.predict(input) 
y_pred = numpy.argmax(y_hat,axis=-1)
print(y_pred.shape)

# calculate the confusion matrix
matrix = confusion_matrix(y_real, y_pred)
print(matrix)
