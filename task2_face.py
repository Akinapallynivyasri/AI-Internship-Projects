
import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

img = cv2.imread('face.jpg')

if img is None:
    print("Error: Image not found. Check file name and location.")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.05,     
    minNeighbors=2,       
    minSize=(30, 30)      
)

print("Number of faces detected:", len(faces))

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.putText(
    img,
    f'Faces: {len(faces)}',
    (20, 40),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 255, 0),
    2
)

cv2.imshow("Face Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()