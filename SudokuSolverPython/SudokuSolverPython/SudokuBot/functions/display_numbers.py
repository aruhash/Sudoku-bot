import cv2


def display_numbers(img, numbers, color=(0, 255, 0)):
    """Displays 81 numbers in the image of the board"""
    W = int(img.shape[1] / 9)
    H = int(img.shape[0] / 9)
    for i in range(9):
        for j in range(9):
            if numbers[(j * 9) + i] != 0:
                cv2.putText(
                    img,
                    str(numbers[(j * 9) + i]),
                    (i * W + int(W / 2) - int((W / 4)), int((j + 0.7) * H)),
                    cv2.FONT_HERSHEY_COMPLEX,
                    2,
                    color,
                    2,
                    cv2.LINE_AA,
                )
    return img
