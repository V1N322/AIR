import cv2
import models

def main():
    cap = cv2.VideoCapture(1)
    fullBody = models.FullBody()

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        fullBody.process(frame)
        data = fullBody.get_data()
        print(data)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()