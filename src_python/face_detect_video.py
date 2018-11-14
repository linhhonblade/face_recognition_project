import cv2

#video_capture = cv2.VideoCapture('/home/hiep/Desktop/github/face-recognition-project/image/video.mp4')
video_capture = cv2.VideoCapture(0)
faceCascade=cv2.CascadeClassifier('/home/hiep/Desktop/github/face-recognition-project/haarcascades/haarcascade_frontalface_default.xml')

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5
    )
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # Display the resulting frame
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
