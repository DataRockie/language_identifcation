
import os.path
import cv2
import glob



for imagepath in glob.glob('C:\Users\sumit\Downloads\hinlan\*'):
##for imagepath in glob.glob('C:\Users\sumit\Downloads\spectro\*'):


            
        img=cv2.imread(imagepath)

      
        img=img[100:700,300:1300]
       
        cv2.imwrite(imagepath,img)
