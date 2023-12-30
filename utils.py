import cv2

def write_image(image, path):
    cv2.imwrite(path, image)

def display_image(image, title = 'Image'):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()