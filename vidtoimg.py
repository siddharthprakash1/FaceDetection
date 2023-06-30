'''
import cv2
import os

cap=cv2.VideoCapture(0)

currentdirectory=os.getcwd()

count = 0
while True:
    ret,test_img=cap.read()
    if not ret :
        continue
    cv2.imwrite(currentdirectory+"/"+"dataset"+"/"+"Sid"+"/"+"frame%d.jpg" % count, test_img)     # save frame as JPG file
    count += 1
    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('face detection Tutorial ',resized_img)
    if cv2.waitKey(10) == ord('q'):#wait until 'q' key is pressed
        break


cap.release()
cv2.destroyAllWindows
'''

'''
import cv2
import os

cap = cv2.VideoCapture(0)

current_directory = os.getcwd()

# Prompt the user to enter the name of the person
person_name = input("Enter the name of the person: ")

# Create a new folder inside the dataset folder
new_folder_path = os.path.join(current_directory, "dataset", person_name)
os.makedirs(new_folder_path, exist_ok=True)

count = 0
while True:
    ret, test_img = cap.read()
    if not ret:
        continue
    cv2.imwrite(os.path.join(new_folder_path, "frame%d.jpg" % count), test_img)  # save frame as JPG file
    count += 1
    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('face detection Tutorial', resized_img)
    if cv2.waitKey(10) == ord('q'):  # wait until 'q' key is pressed
        break

cap.release()
cv2.destroyAllWindows()
'''


import cv2
import os

cap = cv2.VideoCapture(0)

current_directory = os.getcwd()

# Prompt the user to enter the name of the person
person_name = input("Enter the name of the person: ")

# Create a new folder inside the dataset folder
new_folder_path = os.path.join(current_directory, "dataset", person_name)
os.makedirs(new_folder_path, exist_ok=True)

face_cascade = cv2.CascadeClassifier(r"C:\Users\DELL\Desktop\Face-Recognition-with-Python-Dlib-and-Deep-Learning-main\haarcascade_frontalface_default.xml")


count = 0
while True:
    ret, test_img = cap.read()
    if not ret:
        continue

    # Convert the image to grayscale for face detection
    gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Increase the size of the cropped region
        offset = 30  # Adjust this value to control the size of the cropped region
        x -= offset
        y -= offset
        w += 2 * offset
        h += 2 * offset

        # Ensure the cropping dimensions are within the image boundaries
        x = max(0, x)
        y = max(0, y)
        w = min(w, test_img.shape[1] - x)
        h = min(h, test_img.shape[0] - y)
        
        # Crop the detected face region
        cropped_img = test_img[y:y+h+50, x:x+w+50]

        # Save the cropped face image to the new folder
        cv2.imwrite(os.path.join(new_folder_path, "frame%d.jpg" % count), cropped_img)
        count += 1

        # Display the cropped face image
        resized_img = cv2.resize(cropped_img, (300, 300))
        cv2.imshow('Cropped Face', resized_img)

    # Display the original image with face detection rectangles
    cv2.imshow('Face Detection Tutorial', test_img)

    if cv2.waitKey(10) == ord('q'):  # wait until 'q' key is pressed
        break

cap.release()
cv2.destroyAllWindows()



