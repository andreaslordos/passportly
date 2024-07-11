import cv2
import os

def review_images(image_paths):
    rejected_countries = []
    missing_images = []

    for img_path in image_paths:
        if not os.path.exists(img_path):
            print(f"Image does not exist: {img_path}")
            missing_images.append(img_path)
            continue

        image = cv2.imread(img_path)
        if image is None:
            print(f"Failed to load image: {img_path}")
            missing_images.append(img_path)
            continue

        cv2.namedWindow("image")
        cv2.imshow("image", image)

        while True:
            key = cv2.waitKey(0) & 0xFF

            # Press 'y' to accept the image
            if key == ord('y'):
                break

            # Press 'n' to reject the image
            elif key == ord('n'):
                # Extract country code from the image path
                country_code = os.path.basename(os.path.dirname(img_path))
                rejected_countries.append(country_code)
                break

        cv2.destroyAllWindows()

    return rejected_countries, missing_images

if __name__ == "__main__":
    countries = os.listdir("countries")

    image_paths = []
    for c in countries:
        image_paths.append(f'countries/{c}/passport_new__blurred__.png')

    rejected_countries, missing_images = review_images(image_paths)
    print("Rejected country codes:", rejected_countries)
    print("Missing images:", missing_images)
