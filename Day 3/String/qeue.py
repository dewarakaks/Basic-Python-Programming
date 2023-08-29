#make a attendance system using python
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'ImagesAttendance'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)
#function to find the encoding of the images
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        #finding the encoding of the image
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
#function to mark the attendance
def markAttendance(name):
    with open('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        #print(myDataList)
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            #print(nameList)
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')
#calling the function
encodeListKnown = findEncodings(images)
print('Encoding Complete')

#starting the webcam
cap = cv2.VideoCapture(0)

