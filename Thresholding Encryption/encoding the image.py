import cv2
import numpy as np

# Function to hide text using minimal intensity differences
def hide_text(image, text, font_scale=2, thickness=3):
    # Write the text in a barely visible intensity
    hidden_image = image.copy()
    text_size = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)[0]
    text_x = (image.shape[1] - text_size[0]) // 2
    text_y = (image.shape[0] + text_size[1]) // 2
    # Draw the text in intensity slightly darker than the background (e.g., 253 on a 255 background)
    cv2.putText(hidden_image, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, 252, thickness)
    return hidden_image

# Function to add noise to an image
def add_noise(image, mean=0, var=5):
    row, col = image.shape
    sigma = var ** 0.5
    gauss = np.random.normal(mean, sigma, (row, col))
    noisy_image = np.clip(image + gauss, 0, 255).astype(np.uint8)
    return noisy_image

# Create a blank white grayscale image
height, width = 500, 500
image = np.ones((height, width), dtype=np.uint8) * 255  # White background

# Hide the text in the image
hidden_message = "Secret"
hidden_image = hide_text(image, hidden_message)

# Add noise to the hidden image
noisy_image = add_noise(hidden_image)

# Save and display the noisy image
cv2.imwrite('extremely_hidden_noisy_image.png', noisy_image)
cv2.imshow('Extremely Hidden Noisy Image', noisy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
