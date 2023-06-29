import tensorflow as tf 
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt


fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

#print(train_images[0, 23, 23]) #Image one 23 x 23 so the 194th pixel

#print(train_labels[:10])

print(train_images.shape)


class_names = ['T-Shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

'''Show the img:
plt.figure()
plt.imshow(train_images[5])
plt.colorbar()
plt.grid(False)
plt.show() '''

train_images = train_images / 255.0 #squish all the values between 0 and 1, it has to between 0 and 255 cause greyscale image 

test_images = test_images / 255.0

#MODEL:
'''input Layer (1): This is our input layer and it will conist of 784 neurons. 
We use the flatten layer with an input shape of (28,28) to denote that our input should come in in that shape.
The flatten means that our layer will reshape the shape (28,28) array into a vector of 784 neurons so that each
pixel will be associated with one neuron. '''

'''hidden layer (2): This is our first and only hidden layer. The dense denotes that this layer will be fully
   connected and each neuron from the previous layer connects to each neuron of this layer. 
   It has 128 neurons and uses the rectify linear unit activation function. '''

model = keras.Sequential([
	keras.layers.Flatten(input_shape=(28, 28)), #input layer (1), Flatten flattens the 28 x 28 matricie stucture to 784 or whatever 28 x 28 is 
	keras.layers.Dense(128, activation='relu'), #hidden layer (2), the hidden layer is 128 because we want to reduce it by a little asto what the input is, then is using the relu activation f(x)
	keras.layers.Dense(10, activation='softmax') #output layer (3), is given 10 output neurons because thats how many clases there are then its given softmax activation f(x), sofmax makes sure that all of our values add up to one and are between 0 and 1
	])

#COMPILE THE MODEL:

#The last step in building the model is to define the loss function, optimizer and metrics we would like to track

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy']) #how it will calculate the gradient descent basically 

#TRAINING: DFN

#model.fit(train_images, train_labels, epochs=3)

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=1) #verbose how much is getting printed to the console
print('TEST ACC:', test_acc)

predictions = model.predict(test_images)
print(class_names[np.argmax(predictions[5])])

plt.figure()
plt.imshow(test_images[5])
plt.colorbar()
plt.grid(False)
plt.show() 
