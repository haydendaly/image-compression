import numpy as np

# https://q-viper.github.io/2021/05/24/coding-run-length-encoding-in-python/


def compress(img, bits=8, binary=True, view=True):
    """
    img: Grayscale img.
    bits: what will be the maximum run length? 2^bits
    """
    # if binary:
    # ret,img = cv2.threshold(img,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    encoded = []
    count = 0
    prev = None
    th = 127
    for pixel in img:
        if binary:
            if pixel < th:
                pixel = 0
            else:
                pixel = 1
        if prev == None:
            prev = pixel
            count += 1
        else:
            if prev != pixel:
                encoded.append((count, prev))
                prev = pixel
                count = 1
            else:
                if count < (2 ** bits) - 1:
                    count += 1
                else:
                    encoded.append((count, prev))
                    prev = pixel
                    count = 1
    encoded.append((count, prev))

    return np.array(encoded)


def decompress(encoded):
    decoded = []
    for rl in encoded:
        r, p = rl[0], rl[1]
        decoded.extend([p] * r)
    dimg = np.array(decoded)
    return dimg
