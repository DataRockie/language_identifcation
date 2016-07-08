##install the pydub, textblob, glob libraries of python
import os
import glob
from pydub import AudioSegment
import numpy as np
from textblob import TextBlob
##It is the directory in which your audio or video  file exist. Change this directory according your system and rename it as myfile
video_dir = 'C:/Users/sumit/Desktop/stt/testing'  

##list of various extension . You can add your own extension
extension_list = ('*.mp4', '*.flv','*.mp3')

##Convert your file to wav format
os.chdir(video_dir)
for extension in extension_list:
    for video in glob.glob(extension):
        wav_filename = os.path.splitext(os.path.basename(video))[0] + '.wav'
        AudioSegment.from_file(video).export(wav_filename, format='wav')