import sys, os
import pandas as pd
import numpy as np
import cv2
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, BatchNormalization
from keras.losses import categorical_crossentropy
from keras.optimizers import Adam
from keras.regularizers import l2
from keras.callbacks import ReduceLROnPlateau, TensorBoard, EarlyStopping, ModelCheckpoint
from keras.models import load_model
#from tabulate import tabulate

#BASEPATH = 'drive/Emotion Recognition'
#sys.path.insert(0, BASEPATH)
#os.chdir(BASEPATH)
MODELPATH = './models/model.h5'

#emotion_dict = {0: "Angry", 1: "Disgust", 2: "Fear", 3: "Happy", 4: "Sad", 5: "Surprise", 6: "Neutral"}
#emotion_dict = {0: "Angry", 1: "Fear", 2: "Surprise", 3: "Calm"}
emotion_dict = {0: "Angry", 1: "Fear/Surprise", 2: "Calm"}
header = ["Angry", "Fear OR Surprise", "Calm"]

model = load_model(MODELPATH)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
        roi_gray = gray[y:y + h, x:x + w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
        cv2.normalize(cropped_img, cropped_img, alpha=0, beta=1, norm_type=cv2.NORM_L2, dtype=cv2.CV_32F)
        prediction = model.predict(cropped_img)
        print(*header, sep='              ')
        #prediction[0] = "%.2f" % prediction[0]
        formatted_list = []
        for item in prediction[0]:
            formatted_list.append('{percent:.2%}'.format(percent=item))
            #formatted_list.append("%.2f%%" %item)
        #'{percent:.2%}'.format(percent=1.0/3.0)
        print(*formatted_list, sep='\t\t\t')
        
        #print(tabulate(*formatted_list, headers=header))
        #print(['%.1f%%' % x*100 for x in prediction[0]])
        #print('%s: %.1f%%' % (emotion, normalized_prediction[self.emotion_map[emotion]]*100))
        #print(int(np.argmax(prediction)))

        cv2.putText(frame, emotion_dict[int(np.argmax(prediction))], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
        
        print("Emotion: {}, {}".format(int(np.argmax(prediction)), emotion_dict[int(np.argmax(prediction))]))

        print('--------------------------------------------------')
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
