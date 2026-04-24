import cv2 as cv
import pygame
import whatsapp
import time

pygame.mixer.init()
pygame.mixer.music.load("alert.mp3")


class main:
    def video_capture(self, video_path):
        last_sent_time = 0
        cooldown = 15  # seconds between alerts

        cap = cv.VideoCapture(video_path)

        if not cap.isOpened():
            print("Video not opened")
            return

        while True:
            ret, frame = cap.read()
            ret2, frame1 = cap.read()

            if not ret or not ret2:
                break

            diff = cv.absdiff(frame, frame1)
            gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
            _, thresh = cv.threshold(gray, 90, 255, cv.THRESH_BINARY)

            contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

            for c in contours:
                if cv.contourArea(c) > 1500:
                    # draw bounding box
                    x, y, w, h = cv.boundingRect(c)
                    cv.rectangle(frame1, (x, y), (x+w, y+h), (0, 0, 255), 2)

                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.play()

                    current_time = time.time()

                    # send again only after cooldown
                    if current_time - last_sent_time > cooldown:
                        img_name = f"intruder_{int(current_time)}.jpg"
                        cv.imwrite(img_name, frame1)  # use latest frame

                        whatsapp.send_alert()
                        whatsapp.send_image(img_name)

                        last_sent_time = current_time

            cv.imshow("frame", frame1)

            if cv.waitKey(10) == 27:
                break

        cap.release()
        cv.destroyAllWindows()


obj = main()
obj.video_capture("test3.mp4")