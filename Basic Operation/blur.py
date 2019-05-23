import numpy as np
import cv2

img = cv2.imread('../data/lane.jpg')
#print(type(img)) #checking if any error occured

#Gausian Blur
processed_img = cv2.GaussianBlur(img,(3,3),0)
processed_img1 = cv2.GaussianBlur(img,(5,5),0)
processed_img2 = cv2.GaussianBlur(img,(7,7),0)

cv2.imshow('GaussianBlur',processed_img)
cv2.waitKey(1)
cv2.imshow('GaussianBlur1',processed_img1)
cv2.waitKey(1)
cv2.imshow('GaussianBlur2',processed_img2)
cv2.waitKey(0)