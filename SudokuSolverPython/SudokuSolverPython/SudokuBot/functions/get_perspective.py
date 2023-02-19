import cv2, numpy as np


def get_perspective(img, location, height=900, width=900):
    """
    Takes an image and location of interested region.
    Then, returns only the selected region with a perspective transformation.
    """
    pts1 = np.float32([location[0], location[3], location[1], location[2]])
    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

    # Apply the "Perspective Transform" algorithm
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(img, matrix, (width, height))
    return result