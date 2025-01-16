import numpy as np
import cv2
import imageio

cap = cv2.VideoCapture('street.gif')

# Initialize background subtractor
foreground_background = cv2.createBackgroundSubtractorMOG2()

frames = []

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply background subtractor to get our foreground mask
    foreground_mask = foreground_background.apply(frame)

    # Append the frame to the list
    frames.append(foreground_mask)

    cv2.imshow('Output', foreground_mask)
    if cv2.waitKey(100) == 13: 
        break

cap.release()
cv2.destroyAllWindows()

# Save the frames as a looping GIF
imageio.mimsave('output.gif', frames, duration=0.1, loop=0)