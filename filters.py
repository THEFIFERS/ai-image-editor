import cv2

# BLUR FILTER
def apply_blur(image, ksize):

    if ksize > 1:

        image = cv2.GaussianBlur(
            image,
            (ksize, ksize),
            0
        )

    return image


# SHARPNESS FILTER
def apply_sharpness(image, alpha):

    blurred = cv2.GaussianBlur(
        image,
        (0, 0),
        3
    )

    sharpened = cv2.addWeighted(
        image,
        1 + alpha,
        blurred,
        -alpha,
        0
    )

    return sharpened


# BRIGHTNESS FILTER
def apply_brightness(image, beta):

    return cv2.convertScaleAbs(
        image,
        alpha=1,
        beta=beta
    )


# CONTRAST FILTER
def apply_contrast(image, alpha):

    return cv2.convertScaleAbs(
        image,
        alpha=alpha,
        beta=0
    )


# GRAYSCALE FILTER
def apply_grayscale(image):

    gray = cv2.cvtColor(
        image,
        cv2.COLOR_RGB2GRAY
    )

    return gray


# EDGE DETECTION
def apply_edge_detection(image):

    if len(image.shape) == 3:

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_RGB2GRAY
        )

    else:

        gray = image

    edges = cv2.Canny(
        gray,
        100,
        200
    )

    return edges