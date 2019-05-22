import numpy as np
import cv2

img = cv2.imread('../data/lane.jpg')
#print(type(img)) #checking if any error occured

#Gausian Blur
processed_img = cv2.GaussianBlur(img,(5,5),0)




cv2.imshow('GaussianBlur',processed_img)
cv2.waitKey(0)