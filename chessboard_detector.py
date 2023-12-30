import cv2
import numpy as np

def rotate_and_flip_image(image):
    """Rotate the image 180 degrees and flip it."""
    # Rotate the image 180 degrees
    rotated_image = cv2.rotate(image, cv2.ROTATE_180)

    # Flip the image vertically
    flipped_image = cv2.flip(rotated_image, 1)

    # Rotate the image 90 degrees clockwise
    corrected_image = cv2.rotate(flipped_image, cv2.ROTATE_90_CLOCKWISE)

    return corrected_image

def detect_chessboard(image_path):
    """Detect and isolate the chessboard in the given image."""
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply a Gaussian blur to reduce noise and improve edge detection
    gray_blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Threshold the image to get a binary image
    ret, thresh = cv2.threshold(gray_blurred, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Find contours
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    # Sort the contours by area and then by the aspect ratio
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    
    # Assume the largest square-like contour is the chessboard
    for contour in contours:
        # Approximate the contour to a polygon
        perimeter = cv2.arcLength(contour, True)
        approximation = cv2.approxPolyDP(contour, 0.01 * perimeter, True)
        
        # The chessboard should have 4 corners and be somewhat square
        if len(approximation) == 4:
            # Check if the polygon is square-like based on its aspect ratio
            _, _, w, h = cv2.boundingRect(approximation)
            aspectRatio = float(w)/h
            if 0.8 < aspectRatio < 1.2:
                # This is our chessboard
                chessboard_contour = approximation
                break
    
    # Extract the chessboard from the image using the detected contour
    if 'chessboard_contour' in locals():
        # Get the points of the chessboard contour
        points = np.vstack(chessboard_contour).squeeze()
        points = sorted(points, key=lambda x: x[0])  # Sort by x coordinate
        
        # Reorder points to match the perspective transform requirements
        # Top-left, top-right, bottom-right, bottom-left
        if points[0][1] > points[1][1]:
            points[0], points[1] = points[1], points[0]
        if points[2][1] < points[3][1]:
            points[2], points[3] = points[3], points[2]
        pts1 = np.float32([points[0], points[1], points[3], points[2]])
        
        # Define the dimensions of the new image (the extracted chessboard)
        side = max(w, h)
        pts2 = np.float32([[0, 0], [side, 0], [0, side], [side, side]])
        
        # Apply the perspective transformation
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        result = cv2.warpPerspective(image, matrix, (side, side))
        
        # Rotate and flip the extracted chessboard
        corrected_chessboard = rotate_and_flip_image(result)
        
        return corrected_chessboard
    else:
        print("No chessboard found.")
        return None
