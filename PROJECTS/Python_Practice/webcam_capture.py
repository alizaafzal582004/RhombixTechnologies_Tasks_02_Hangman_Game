import cv2

# Open the webcam (0 = default camera)
cam = cv2.VideoCapture(0)

cv2.namedWindow("Webcam Capture")

img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("Webcam Capture", frame)

    # Press 'q' to quit
    k = cv2.waitKey(1)

    if k % 256 == ord('q'):
        print("Closing...")
        break

    # Press 's' to save a photo
    elif k % 256 == ord('s'):
        img_name = f"photo_{img_counter}.png"
        cv2.imwrite(img_name, frame)
        print(f"{img_name} saved!")
        img_counter += 1

cam.release()
cv2.destroyAllWindows()
