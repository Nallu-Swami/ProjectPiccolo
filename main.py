import cv2

def display_webcam_feed():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('Webcam Feed', frame)

        # Check for the 'q' key to quit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()

# Call the function to start displaying the webcam feed
display_webcam_feed()