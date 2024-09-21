import cv2
import mediapipe as mp
import math

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def camrec():
    frame_count = 0  # Initialize frame count
    output = 96000/2
    while True:
        success, frame = cap.read()
        if not success:
            break

        # Flip the frame to avoid mirror effect
        frame = cv2.flip(frame, 1)

        # Convert the frame to RGB for Mediapipe processing
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        # Increment frame count every frame
        frame_count += 1

        # Check if any hand is detected
        if results.multi_hand_landmarks:
            for i, hand_landmarks in enumerate(results.multi_hand_landmarks):
                # Draw landmarks on the frame
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Get handedness (Left or Right hand)
                hand_label = results.multi_handedness[i].classification[0].label

                # Get thumb and index landmarks
                thumb_tip = hand_landmarks.landmark[4]  # Thumb tip
                index_tip = hand_landmarks.landmark[8]  # Index finger tip

                # Convert normalized coordinates to pixel values
                thumb_x = int(thumb_tip.x * 640)
                thumb_y = int(thumb_tip.y * 480)
                index_x = int(index_tip.x * 640)
                index_y = int(index_tip.y * 480)

                # Calculate the Euclidean distance between thumb and index
                distance = math.hypot(index_x - thumb_x, index_y - thumb_y)
                

                # Every 15 frames, print distance and brightness
                if frame_count >= 15:
                    if hand_label == 'Right':
                        # print(f"Right hand distance: {distance}")
                        distance_ratio = distance / 200
                        if distance_ratio < 1:
                            output = distance_ratio * 96000
                        else:
                            output = 96000
                        
                    elif hand_label == 'Left':
                        print(f"Left hand distance: {distance}")
                    
                    # Reset frame count after processing
                    frame_count = 0

                yield output  # Yield the result from camrec

                # Optionally draw the hand type (Left or Right) on the frame
                cv2.putText(frame, hand_label, (10, 50 + i * 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
        # Display the frame with hand landmarks
        cv2.imshow("Hand Tracking", frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and close all windows
    cap.release()
    cv2.destroyAllWindows()

class TheOutputGiver:
    def __init__(self):
        self.camout = camrec()  # Initialize the camrec generator

    def looper(self):
        while True:
        
            finalout = next(self.camout)  # Fetch the next output from camrec
            # print(finalout)  # Print the resultq
            yield finalout  # Yield the result continuously
        

# Create an instance of TheOutputGiver
output_giver = TheOutputGiver()

# Run the looper method to continuously get output
