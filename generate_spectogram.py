
import os
import wave
import glob
import pylab
def graph_spectrogram(imagepath):
    image,ID=imagepath[imagepath.rfind("/")+6:].split('.')
    print image
    sound_info, frame_rate = get_wav_info(imagepath)
    
    pylab.figure(num=None, figsize=(19, 12))
    pylab.subplot(111)
    ##pylab.title('spectrogram of %r' % imagepath)
    pylab.specgram(sound_info, Fs=frame_rate)
    pylab.savefig('C:/Users/sumit/Downloads/hinlan/'+image+'.png')
    ##pylab.savefig('C:/Users/sumit/Downloads/spectro/'+image+'.png')
def get_wav_info(wav_file):
    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    sound_info = pylab.fromstring(frames, 'Int16')
    frame_rate = wav.getframerate()
    wav.close()
    return sound_info, frame_rate
if __name__ == '__main__':
   for imagepath in glob.glob('C:/Users/sumit/Downloads/hindi/*'): 
   ##for imagepath in glob.glob('C:/Users/sumit/Downloads/english/*'):
       ##imagepath = 'C:/Users/sumit/Downloads/english/boy.wav'
       graph_spectrogram(imagepath)