import cv2 

# Import uuid
import uuid

# Import Operating System
import os

# Import time
import time

IMAGES_PATH = 'C:\\Users\\yashi\\Pictures\\sign detection\\sign detection yashika\\Tensorflow\\workspace\\images\\collectedimages'

labels = ['hello', 'thanks', 'iloveyou', 'yes', 'no']
number_imgs = 10

for label in labels:
    os.mkdir('C:\\Users\\yashi\\Pictures\\sign detection\\sign detection yashika\\Tensorflow\\workspace\\images\\collectedimages\\'+label)
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(10): 
        print('Collecting image {}'.format(imgnum))
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH,label,label+'.'+'{}.jpg'.format(imgnum))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
