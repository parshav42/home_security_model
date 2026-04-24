import cv2 as cv
import pygame

pygame.mixer.init()
pygame.mixer.music.load("alert.mp3")  # add your sound file


class main:
    def video_capture(self, video_path):

        cap = cv.VideoCapture(video_path)

        if not cap.isOpened():
            print("❌ Video not opened")
            return

        while True:
            ret, frame = cap.read()
            ret2, frame1 = cap.read()

            if not ret or not ret2:
                break

            diff = cv.absdiff(frame, frame1)
            gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
            _, thresh = cv.threshold(gray, 20, 255, cv.THRESH_BINARY)

            contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


            for c in contours:
                if cv.contourArea(c) > 500:
                    # 🔊 play alarm only when motion detected
                    if not pygame.mixer.music.get_busy():
                        pygame.mixer.music.play()

            cv.imshow("frame", thresh)

            if cv.waitKey(10) == 27:
                break

        cap.release()
        cv.destroyAllWindows()


obj = main()
obj.video_capture("test3.mp4")

