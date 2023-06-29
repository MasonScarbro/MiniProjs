import tensorflow as tf  
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from six.moves import urllib
import tensorflow.compat.v2.feature_column as fc

#survived is the label and the rest are features, go figure 
#paying attention to the dataset we need to know what data correlates to what
dftrain = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv') # the dataset fro training the model
dfeval = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv') # a smaller evaluating dataset 
y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived') #pops and returns the value, basically removed from the data and assigns it to the val

CATEGORIAL_COLUMNS = ['sex', 'n_siblings_spouses', 'parch',
					 'class', 'deck', 'embark_town', 'alone'] # the columns without numerice values

NUMERIC_COLUMNS = ['age', 'fare'] #The Columns with Numerice values 

feature_columns = [] #what needs to be feed to the model

for feature_name in  CATEGORIAL_COLUMNS:
	'''This searches through the data set looking 
	   for each feature in the categorial columns
	   and .unique stores teh unique values in an array, not a number'''

	vocabulary = dftrain[feature_name].unique() 
	'''This second one is just something youll never memorize the syntax for
	   but essiantially what it does is it creates a feature column which we need obvi
	   and this long ass function call basically appends the column with the feature name and its assigned vocabulary
	   basically it adds each feature_name and then adds the vocab assigned''' 
	feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name, vocabulary))

for feature_name in NUMERIC_COLUMNS:
	feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))

#data_df: the dataframe we will feed it, the pandas df in this case
#label_df: our dataframe label, the output we want,m in other words the label
#num_epochs: the number of epochs we will run through, default is 10
#shuffle: whether we will shuffle the data each epoch
#batch_size: the actual amount of data for each epoch, the batch of data

def make_input_fn(data_df, label_df, num_epochs=10, shuffle=True, batch_size=32):
  def input_function():  # inner function, this will be returned
  	#The ds essiantially passes a dictionary representation of our dataframe and pases teh label dataframe, so the  ouput '''
    ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))  # create tf.data.Dataset object with data and its label
    if shuffle:
      ds = ds.shuffle(1000)  # randomize order of data
      '''takes the dataset and splits it into a number of "blocks" that get passed into 
      	 our model and the fucntion figures out how many blocks it needs to break it into in order to train'''
    ds = ds.batch(batch_size).repeat(num_epochs)  # split dataset into batches of 32 and repeat process for number of epochs
    return ds  # return a batch of the dataset
  return input_function  # return a function object for use

#since the make input func makes a function we can call we need to make those functions here 
#the values for the training are set to default
train_input_fn = make_input_fn(dftrain, y_train, num_epochs=180, shuffle=True, batch_size=40)  # here we will call the input_function that was returned to us to get a dataset object we can feed to the model
eval_input_fn = make_input_fn(dfeval, y_eval, num_epochs=1, shuffle=False) # since this is the eval function we dont need to have any epochs or shuffle it

linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns) # This creates an estimator and passes the feature columns in to create the model

#TRAINING:

'''The input function we created earlier is actually equal to a function itself so it actually calls the function
   so we pass the function in and it will grab all the input  that it needs and train the function'''

linear_est.train(train_input_fn) #calls the train function call and well, trains it see documentation
result = linear_est.evaluate(eval_input_fn) # The result is the evaluated metrics and stats of the model

clear_output()
print(result['accuracy'])
'''
result = list(linear_est.predict(eval_input_fn))


print(dfeval.loc[4])
print(y_eval.loc[4]) # the actual survive on the eval
print(result[4]['probabilities'][1]) # the prediction on wether the person will survive or not 0 
'''
