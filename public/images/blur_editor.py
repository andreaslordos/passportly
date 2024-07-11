import cv2
import os

# Function to blur the region within the bounding box
def blur_region(image, start_point, end_point):
    x1, y1 = start_point
    x2, y2 = end_point
    region = image[y1:y2, x1:x2]
    blurred_region = cv2.GaussianBlur(region, (99, 99), 0)
    image[y1:y2, x1:x2] = blurred_region
    return image

# Mouse callback function to draw rectangle
def draw_rectangle(event, x, y, flags, param):
    global start_point, end_point, drawing, image, original_image

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_point = (x, y)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img_copy = image.copy()
            cv2.rectangle(img_copy, start_point, (x, y), (0, 255, 0), 2)
            cv2.imshow("image", img_copy)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        end_point = (x, y)
        cv2.rectangle(image, start_point, end_point, (0, 255, 0), 2)
        cv2.imshow("image", image)
        blur_region(image, start_point, end_point)

# Main function to process images
def process_images(image_paths):
    global image, start_point, end_point, drawing, original_image
    for img_path in image_paths:
        original_image = cv2.imread(img_path)
        if original_image is None:
            print(f"Failed to load image: {img_path}")
            continue
        
        image = original_image.copy()
        cv2.namedWindow("image")
        cv2.setMouseCallback("image", draw_rectangle)
        drawing = False
        start_point, end_point = (0, 0), (0, 0)

        while True:
            cv2.imshow("image", image)
            key = cv2.waitKey(1) & 0xFF

            # Press Enter key to save the image
            if key == 13:  # Enter key
                dir_name, file_name = os.path.split(img_path)
                base_name, ext = os.path.splitext(file_name)
                new_file_name = f"{base_name}__blurred__{ext}"
                output_path = os.path.join(dir_name, new_file_name)
                cv2.imwrite(output_path, image)
                print(f"Image saved: {output_path}")
                break

            # Press 'q' to exit
            elif key == ord('q'):
                break

            # Press 'esc' to undo all boxes
            elif key == 27:  # Esc key
                image = original_image.copy()
                cv2.imshow("image", image)

        cv2.destroyAllWindows()

if __name__ == "__main__":
    import sys
    # countries = os.listdir("countries")
    # countries = ['ye', 'zm', 'sy', 'sd', 'pk', 'uz', 'pw', 'py', 'km', 'mg', 'cg', 'lc', 'it', 'to']
    # countries = ['mu', 'mr', 'bj', 'kw', 'ae', 'ci', 'in', 'ee', 'tl', 'qa', 'tm', 'td', 'ro', 'st', 'pt', 'sr', 'uy', 'sg', 'ph', 'bh', 'ht', 'bt', 'gq', 'bi', 'br', 'mv', 'iq', 'er', 'tt', 'ws']
    countries = ['mr', 'qa', 'td', 'ro', 'pt'] + ['pw', 'py', 'lc', 'it']

    image_paths = []
    for c in countries:
        image_paths.append(f'countries/{c}/passport_new.png')

    process_images(image_paths)
