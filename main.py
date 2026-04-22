from os.path import exists

import cv2 as cv
from ultralytics import YOLO
import os

os.makedirs("outputs",exist_ok=True)


class main:
    def video_capture(self, video_path):

        cap = cv.VideoCapture(video_path)
        count =0
        model = YOLO('yolo26n.pt')
        face_cascade = cv.CascadeClassifier(
            cv.data.haarcascades + "haarcascade_frontalface_default.xml"
        )
        if face_cascade.empty() & cap.isOpened():
            print("❌ Face cascade not loaded or video not opened")
            exit()
        # if not cap.isOpened():
        #     print("Video not available")
        #     return
        while True:
            ret, frame = cap.read()
            result = model.predict(frame ,classes = [0])
            for box in result[0].boxes:
                x1,y1,x2,y2 = map(int , box.xyxy[0])
                person_roi = frame[y1:y2,x1:x2]

                gray = cv.cvtColor(person_roi,cv.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, 1.1, 5)
                for (fx,fy,fw,fh) in faces:
                    fase_crop = person_roi[fy:fy+fh,fx:fx+fw]
                    filename = f"outputs/{count}.png"
                    cv.imwrite(filename,fase_crop)
                    count += 1
                    cv.rectangle(frame,(x1 +fx , y1+fy),(x1+fx+fw,y1+fy+fh),(0,255,0),2)



            cv.imshow("frame",frame)
            if cv.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv.destroyAllWindows()
obj = main()
obj.video_capture('test3.mp4')



        

