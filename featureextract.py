
import cv2
import glob
output=open('feat.csv', 'w+')

 

output.write('{0},{1}\n'.format('ImageId','Label','Image')) 
##output.write('{0},{1}\n'.format('ImageId','Image')) 
##for imagepath in glob.glob('C:/Users/sumit/Downloads/spectro/*'):
for imagepath in glob.glob('C:/Users/sumit/Downloads/hinlan/*'):
##imagepath='C:/Users/sumit/Downloads/spectro/above.png'
    imageID=imagepath[imagepath.rfind("/")+1:]
    ##print imageID
    
    Label='english'
    
    image=cv2.imread(imagepath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    h,w=gray.shape
    ##cv2.imshow('img',image)
    output.write('{0},{1},'.format(imageID,Label))
    for x in range(w):
            for y in range(h):
                   r = gray[y,x]
                   output.write('{0} '.format(r))

    output.write('\n ')

##feature=[str(f) for f in feature]



"""
feature=[str(f) for f in feature]
output.write("%s,%s\n" % (imageID,",".join(feature)))
"""
    
output.close()   