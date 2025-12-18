import cv2
import time
import os

if not os.path.exists("faces"):
    os.makedirs("faces")

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

# 🔴 IMPORTANT: use CAP_DSHOW + set resolution
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("❌ Camera not opened")
    exit()

face_id = 0
last_saved_time = 0
SAVE_INTERVAL = 2

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        print("❌ No frame received")
        continue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    current_time = time.time()

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)

        if len(eyes) > 0 and (current_time - last_saved_time) > SAVE_INTERVAL:
            face_id += 1
            cv2.imwrite(f"faces/face_{face_id}.jpg", frame[y:y+h, x:x+w])
            last_saved_time = current_time

    cv2.putText(
        frame,
        f"Faces: {len(faces)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Face Detection", frame)

    # 🔴 REQUIRED for window refresh
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
