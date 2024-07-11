import cv2
import pytesseract
from pytesseract import Output
import os

def blur_letters(country):
    # Get path
    image_path = f"public/images/countries/{country}/passport_new.png"
    
    # Load the image
    img = cv2.imread(image_path)
    
    # Convert the image to RGB (pytesseract requires RGB images)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Use pytesseract to detect letters and their bounding boxes
    details = pytesseract.image_to_data(img_rgb, output_type=Output.DICT)
    
    num_boxes = len(details['text'])
    for i in range(num_boxes):
        # Extract bounding box coordinates
        (x, y, w, h) = (details['left'][i], details['top'][i], details['width'][i], details['height'][i])
        
        # Check if the detected object is textual and not empty/whitespace
        if details['text'][i].strip():
            # Blur the area of the letter
            img[y:y+h, x:x+w] = cv2.blur(img[y:y+h, x:x+w], (25, 25))
    
    # Save or display the blurred image
    cv2.imwrite(f"public/images/countries/{country}/passport_blurred_new.jpg", img)
    # cv2.imshow('Blurred Image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


# Example usage
# blur_letters('path_to_your_image.jpg')
country_list = os.listdir("public/images/countries")

for country in country_list:
    print(country)
    blur_letters(country)
