import keras
import numpy as np
from keras.models import load_model
from keras.datasets import imdb




#dictoinery
word_to_id = keras.datasets.imdb.get_word_index()
#loading the model ***
model = load_model('your_new_model.h5')

a = input("Enter a review\n")

b = []
for i in a.split():
  try:
    b.append(word_to_id[i])
  except:
    pass

b = np.array(b)

def multi_hot_encode(sequences, dimension):

  
  results = np.zeros(dimension)
  for i in range(len(sequences)):
  	results[i] = 1
  return results

validation = multi_hot_encode(b, 10000)
validation = np.array([validation])
print("Negative, Positive")
print(model.predict(validation))