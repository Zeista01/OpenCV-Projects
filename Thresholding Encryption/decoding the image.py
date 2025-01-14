import cv2 
# Function to reveal text using precise thresholding
def reveal_text(noisy_image):
    # Apply thresholding with a low threshold to reveal the subtle intensity differences
    _, revealed_image = cv2.threshold(noisy_image, 252, 255, cv2.THRESH_BINARY)
    return revealed_image

# Load the noisy image
noisy_image = cv2.imread('extremely_hidden_noisy_image.png', cv2.IMREAD_GRAYSCALE)

# Reveal the hidden text
revealed_image = reveal_text(noisy_image)

# Save and display the revealed image
cv2.imwrite('revealed_extremely_hidden_text.png', revealed_image)
cv2.imshow('Revealed Extremely Hidden Text', revealed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
