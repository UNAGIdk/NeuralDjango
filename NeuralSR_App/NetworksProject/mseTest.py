import numpy as np
import cv2

imageA = cv2.imread('demo/manHR.jpg')
imageB = cv2.imread('resources/Super Image EDSR.jpg')

# the 'Mean Squared Error' between the two images is the
# sum of the squared difference between the two images;
# NOTE: the two images must have the same dimension
err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
err /= float(imageA.shape[0] * imageA.shape[1])
print("MSE score is: " + str(err))

# return the MSE, the lower the error, the more "similar"
# the two images are
