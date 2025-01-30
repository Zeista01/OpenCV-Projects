import cv2
import pygame

pygame.init()
image = r"./Kano.jpg"
scale = 1  # Set scale to 1 to display the image at its original size
bgr_img = cv2.imread(image)
bgr_img = cv2.resize(bgr_img, None, fx=scale, fy=scale)
hsv_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV)
breadth, length, _ = bgr_img.shape

# Set the window size to match the image dimensions
win = pygame.display.set_mode((length, breadth))
pygame.display.set_caption("Image Color Picker")
font = pygame.font.SysFont("Arial", 20)
bkg = pygame.surfarray.make_surface(cv2.transpose(cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)))

# Function to pixelate the image
def pixelate_image(image, pixel_size):
    height, width, _ = image.shape
    pixelated_image = image.copy()
    for y in range(0, height, pixel_size):
        for x in range(0, width, pixel_size):
            end_x = min(x + pixel_size, width)
            end_y = min(y + pixel_size, height)
            block = image[y:end_y, x:end_x]
            avg_color = block.mean(axis=(0, 1)).astype(int)
            pixelated_image[y:end_y, x:end_x] = avg_color
    return pixelated_image

# Initialize variables
run = True
pixelated_mode = False
pixel_size = 10
pixelated_img = bgr_img.copy()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Toggle Pixelation mode
                pixelated_mode = not pixelated_mode
                if pixelated_mode:
                    pixelated_img = pixelate_image(bgr_img, pixel_size)
            if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:  # Increase pixel size
                pixel_size = min(pixel_size + 5, max(breadth, length) // 2)
                if pixelated_mode:
                    pixelated_img = pixelate_image(bgr_img, pixel_size)
            if event.key == pygame.K_MINUS or event.key == pygame.K_UNDERSCORE:  # Decrease pixel size
                pixel_size = max(pixel_size - 5, 1)
                if pixelated_mode:
                    pixelated_img = pixelate_image(bgr_img, pixel_size)
            if event.key == pygame.K_s:
                cv2.imwrite('pixel_art.jpg', cv2.cvtColor(pixelated_img, cv2.COLOR_RGB2BGR))

            

    # Get mouse position
    x, y = pygame.mouse.get_pos()
    b, g, r = bgr_img[y][x]
    h, s, v = hsv_img[y][x]

    # Render text for RGB and HSV values
    text_1 = font.render(f"RGB = {r}, {g}, {b}", True, (255,255,255))
    text_2 = font.render(f"HSV = {h}, {s}, {v}", True, (255,255,255))
    x1, y1 = text_1.get_size()
    x2, y2 = text_2.get_size()
    l = max(x1, x2)
    h = max(y1, y2)

    temp_surf = pygame.Surface((l, h*2))
    temp_surf.fill((0,0,0))
    temp_surf.blit(text_1, (0,0))
    temp_surf.blit(text_2, (0, h))

    # Display the image
    display_img = pixelated_img if pixelated_mode else bgr_img
    bkg = pygame.surfarray.make_surface(cv2.transpose(cv2.cvtColor(display_img, cv2.COLOR_BGR2RGB)))
    win.blit(bkg, (0,0))

    # Display text near the mouse cursor
    plotx = x + 10
    ploty = y + 10
    if plotx + l > length:
        plotx = x - l - 10
    if ploty + h * 2 > breadth:
        ploty = y - h * 2 - 10
    win.blit(temp_surf, (plotx, ploty))
    pygame.display.update()

pygame.quit()
