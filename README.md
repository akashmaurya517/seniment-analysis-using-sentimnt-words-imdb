# seniment-analysis-using-sentimnt-words-imdb
sentiment analysis on imdb data set with a deferent aproach
the imdb data set is of most of the hollywood movies and the reviews are aslo by most of the USA citizens.
thats why this model become biesed towards wastern culture and their accent of speaking and writing.

ini this model i have used some sentiment lexicons by indian commumnity that desides the sentence to be positive or negative 

## sentiment lexicons
sentiment lexicons are some bag of words that has both positive and negative labled words 
you can see that in **positive words.txt** and **negative words.txt** files

using these lexicons and then making the model

## **HOW TO USE THIS REPO?**

### step 1:
set up internet connection and your environmentshaving following dependencies
1. tensorflow
2. numpy
4. h5py
5. maths
6. keras
please do install others if you need
### step  2:
Run **Sentiment_Analysis_training_new.py** file first

### step 3:
now Run  **Sentiment_Analysis_new.py** file to get result
## Result
the result will be the array of two elements 
### first element of the array will be showing the pobability of being the sentence or review negative 
### the second element of array is the probability of being the sentence or review positive

the **Sentiment_Analysis_new.ipynb** file is the python noteboomk developement file for this project
