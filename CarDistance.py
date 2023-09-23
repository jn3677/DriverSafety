import cv2
import winsound  # Import the winsound module
import queue

# Initialize the camera (you may need to configure this based on your camera setup)
cap = cv2.VideoCapture(0)  # 0 represents the default camera

# Set the known width of the car in front (in meters)
known_car_width = 2.0  # Example: 2 meters

# Set the focal length of the camera (you'll need to calibrate this)
# Focal length = (width of the object in pixels * distance to the object) / known_car_width
focal_length = 1000.0  # Example: 1000 pixels

# Create an audio queue for alerts
audio_queue = queue.Queue()

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Perform object detection and find the car in front
    # (You should use a pre-trained object detection model here)

    # Calculate the width of the car in pixels
    # (You can get this information from the object detection result)
    car_width_pixels = 100  # Example: 100 pixels

    # Calculate the distance to the car in front (in meters)
    distance = (known_car_width * focal_length) / car_width_pixels

    # Set a safe following distance threshold (in meters)
    safe_distance = 5.0  # Example: 5 meters

    # Check if the vehicle is too close to the car in front
    if distance < safe_distance:
        # Trigger an audio alert and add it to the audio queue
        audio_queue.put("alert.wav")  # Replace with your audio alert file

    # Play audio alerts from the queue
    while not audio_queue.empty():
        alert_sound = audio_queue.get()
        winsound.PlaySound(alert_sound, winsound.SND_FILENAME)

    # Display the frame with detected objects and distance information
    cv2.imshow('Distance Detection', frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()