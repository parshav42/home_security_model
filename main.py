import cv2 as cv
import pygame
import bot
import time
import os
from ultralytics import YOLO as y

model = y("yolov8n.pt")

pygame.mixer.init()
pygame.mixer.music.load("alert.mp3")

os.makedirs("output", exist_ok=True)

class main:
    def video_capture(self, video_path):
        last_sent_time = 0
        cooldown = 4

        cap = cv.VideoCapture(video_path)

        if not cap.isOpened():
            print("Video not opened")
            return

        while True:

            ret, frame = cap.read()
            ret2, frame1 = cap.read()
            result = model(frame)
            for r in result:
                boxes = r.boxes

                for box in boxes:
                    cls =int(box.cls[0])

                    if cls == 0:
                        x1,y1,x2,y2=map(int ,box.xyxy[0])
                        cv.rectangle(frame, (x1,y1),(x2,y2), (0, 0, 255), 2)
                        cv.putText(frame,"Person",(x1,y1-10),cv.FONT_HERSHEY_PLAIN,0.8,(0,255,0),2)
            if not ret or not ret2:
                break

            diff = cv.absdiff(frame, frame1)
            gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
            _, thresh = cv.threshold(gray, 50, 255, cv.THRESH_BINARY)

            # contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

            # for c in contours:
            #     if cv.contourArea(c) > 4000:
            #         # draw bounding box
            #         x, y, w, h = cv.boundingRect(c)
            #         cv.rectangle(frame1, (x, y), (x+w, y+h), (0, 0, 255), 2)
            #
            #         # if not pygame.mixer.music.get_busy():
            #         #     pygame.mixer.music.play()
            #
            #         current_time = time.time()
            #
            #
            #         if current_time - last_sent_time > cooldown:
            #             img_name = f"output/intruder_{int(current_time)}.jpg"
            #             cv.imwrite(img_name, frame1)  # use latest frame
            #
            #             bot.send_alert()
            #             bot.send_image(img_name)
            #
            #             last_sent_time = current_time

            cv.imshow("Home Camera", frame)

            if cv.waitKey(1) == 27:
                break

        cap.release()
        cv.destroyAllWindows()


obj = main()
obj.video_capture(1)


