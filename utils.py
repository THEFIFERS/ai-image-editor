import cv2
import numpy as np
from PIL import Image


# LOAD IMAGE
def load_image(uploaded_file):

    image = Image.open(
        uploaded_file
    ).convert("RGB")

    return np.array(image)


# CONVERT IMAGE TO BYTES
def image_to_bytes(image):

    # GRAYSCALE IMAGE
    if len(image.shape) == 2:

        success, buffer = cv2.imencode(
            ".png",
            image
        )

    else:

        image_bgr = cv2.cvtColor(
            image,
            cv2.COLOR_RGB2BGR
        )

        success, buffer = cv2.imencode(
            ".png",
            image_bgr
        )

    return buffer.tobytes()