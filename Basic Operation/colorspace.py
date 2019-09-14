import numpy as np
import cv2
import os

img = cv2.imread('../data/lane.jpg')
img = cv2.GaussianBlur(img,(7,7),0)

# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

##Calculating HSV value for yellow
yellow = np.uint8([[[0,255,255 ]]]) #BRG
hsv_yellow = cv2.cvtColor(yellow, cv2.COLOR_BGR2HSV)
print(hsv_yellow)

# # define range of yellow color in HSV
# lowerYellow = np.array([20,100,100],dtype="uint8")
# upperYellow = np.array([40,255,255],dtype="uint8")

# # Threshold the HSV image to get only yellow colors
# mask = cv2.inRange(hsv, lowerYellow, upperYellow)

#https://www.learnopencv.com/color-spaces-in-opencv-cpp-python/

# Range for lower red
lower_red = np.array([0,120,70])
upper_red = np.array([10,255,255])
mask1 = cv2.inRange(hsv, lower_red, upper_red)
 
# Range for upper range
lower_red = np.array([170,120,70])
upper_red = np.array([180,255,255])
mask2 = cv2.inRange(hsv,lower_red,upper_red)

mask = mask1 + mask2
# Bitwise-AND mask and original image
res = cv2.bitwise_and(img,img, mask= mask)
cannyImage = cv2.Canny(res,50,150)

cv2.imshow('RGB',img)
cv2.imshow('hsv',hsv)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
cv2.imshow('canny',cannyImage)
cv2.waitKey(0)