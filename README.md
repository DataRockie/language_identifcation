# language_identifcation
assignment for language identification in a mp3 file.
1.>microphone_audio_generator.py -- this  program can be used to generate our own audio for the testing
2.>to_wmvconvert.py -- This program converts a file(mp3, mp4, wmv) into a wav file
3.>generate_spectogram.py -- this program converts a wav file into spectogram
4.>featureextract.py -- this program is used to extract features from the  the spectogram .. I converted a spectogram image into pixels 
5.>re.py -- this program is to resize the image
6.>voice_identity.py -- this program extract data from the csv file and train our model using various classifier(I have implemented here SVM only) . 

This model is just the demo .. it will not work properly due the unavailibility of dataset .. I am trying implementing nueral net(deep learning).
The deep learning is the best model for this.
It automatically extracts best features from a training database and the classification accuracy is also better
as compared to other models.
