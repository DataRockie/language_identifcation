# language_identifcation
assignment for language identification in a mp3 file.
microphone_audio_generator.py -- this  program can be used to generate our own audio for the testing
to_wmvconvert.py -- This program converts a file(mp3, mp4, wmv) into a wav file
generate_spectogram.py -- this program converts a wav file into spectogram
featureextract.py -- this program is used to extract features from the  the spectogram .. I converted a spectogram image into pixels 
re.py -- this program is to resize the image
voice_identity.py -- this program extract data from the csv file and train our model using various classifier(I have implemented here SVM only) . 

This model is just the demo .. it will not work properly due the unavailibility of dataset .. I am trying implementing nueral net(deep learning).
The deep learning is the best model for this.
It automatically extracts best features from a training database and the classification accuracy is also better
as compared to other models.
