
Title: Generate lyrics for your favorite singer

Collaborators: Jarra Omar, Orlando Cedeno

Abstract: The goal of this project is to generate lyrics for a favorite singer of your choice. For our data, we used Genius's API to load artists and a collection of their songs into a csv file. From there, after some pre-processing of the text we were able to train a deep learning model to generate new lyrics based on the patterns and themes found in the existing lyrics.

genius.ipynb: Create a Data file directory in the project structure that holds the artist you're looking for in the form of "kanye.txt". Iterate through that file directory, which will allow you to search the genius api for all the songs the artist has (currently limited to 10). It then places the songs in a song folder for a given artist. For example, "songs/Kanye West" which has the songs for this artist and its lyrics within a text file

lyricgenerator.ipnyb: Searches through the song folder and iterates through each artists and adds each individual song into a big csv, columned into ['Artist'] and ['Lyric']. From there each song is pre-processed to get rid of stop words, unknown characters, stemm words, and ultimately clean the lyrics in prep for training the model. This is then placed into a preprocessed_lyric.csv. We then tokenize each lyric found in this csv file, label encode each artist, and split the data into training, testing, and validation (which can be found in data_splits for further examination). From there we load the data and create a MLP model. After we one-hot encode the target variable and add early stopping. We run and test the model's accuracy for the small subset of 10 songs which is available at the moment.

Genius File: This file uses Geniuses API in order to collect
