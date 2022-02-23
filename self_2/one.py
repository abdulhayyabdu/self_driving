import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny(image):
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny
def display_line(image,lines):
    line_image=np.zeros_like(image)
    if lines is not None:
        for line in lines:

            x1, y1, x2, y2=line.reshape(1,1)
            cv2.line(line_image,(x1, y1),(x1,y2),(255,0,0),10)
    return line_image

def region_of_interest(image):
    height=image.shape[0]
    polygons=np.array([
    [(200, height), (1100, height),(550,250)]
    ])
    mask=np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image=cv2.bitwise_and(canny,mask)
    return masked_image

image=cv2.imread('test_image.jpg')
lane_image=np.copy(image)
canny=canny(lane_image)
cropped_image=region_of_interest(canny)
minLineLength=40
maxLineGap=5
lines=cv2.HoughLines(cropped_image,2,np.pi/180, 100,np.array([]),minLineLength,maxLineGap)
print(lines[0].shape)
print(lines[0])
print(type(lines))
line_image=display_line(lane_image,lines)
combo_image=cv2.addWeighted()
cv2.imshow("results",line_image )

cv2.waitKey(0)