import numpy as np
import cv2
import os

img = cv2.imread('../data/lane.jpg')
#print(type(img)) #checking if any error occured
#Gausian Blur https://docs.opencv.org/3.1.0/d4/d13/tutorial_py_filtering.html
#Blur Types:Averaging, GaussianBlur, Median Blurring, Bilateral Filtering
def Average():
	print("blur(InputArray src,OutputArray dst,Size ksize,Point anchor = Point(-1,-1),int borderType = BORDER_DEFAULT ")
	while(True):
		kernel = tuple(map(int,input('Enter kernel value in format x,x :').split(',')))
		blurred_img = cv2.blur(img,kernel)
		canny_img = cv2.Canny(blurred_img,50,150)
		cv2.imshow('Blured Image',blurred_img)
		cv2.waitKey(1)
		cv2.imshow('Blur effect in Canny',canny_img)
		cv2.waitKey(1)
		ans = input("Try again?[y/n]")
		if (ans=='n'):
			return

def Gaussian():
	print("GaussianBlur(InputArray src,OutputArray dst,Size ksize,double sigmaX,double sigmaY = 0,int borderType = BORDER_DEFAULT)")
	while(True):
		kernel = tuple(map(int,input('Enter kernel value in format x,x :').split(',')))
		blurred_img = cv2.GaussianBlur(img,kernel,0)
		canny_img = cv2.Canny(blurred_img,50,150)
		cv2.imshow('Blured Image',blurred_img)
		cv2.waitKey(1)
		cv2.imshow('Blur effect in Canny',canny_img)
		cv2.waitKey(1)
		ans = input("Try again?[y/n]")
		if (ans=='n'):
			return

def MedianBlur():
	print("medianBlur(InputArray src,OutputArray dst,int ksize)")
	while(True):
		ksize = int(input('Enter ksize, greater than 1 and odd:'))
		blurred_img = cv2.medianBlur(img,ksize)
		canny_img = cv2.Canny(blurred_img,50,150)
		cv2.imshow('Blurred Image',blurred_img)
		cv2.waitKey(1)
		cv2.imshow('Blur effect in Canny',canny_img)
		cv2.waitKey(1)
		ans = input("Try again?[y/n]")
		if (ans=='n'):
			return

def BilateralFilter():
	print("bilateralFilter(InputArray src,OutputArray dst,int d,double sigmaColor,double sigmaSpace,int borderType = BORDER_DEFAULT)")
	while(True):
		d= int(input('Enter d:'))
		sigmaColor= int(input('Enter sigmaColor:'))
		sigmaSpace= int(input('Enter sigmaSpace:'))
		blurred_img = cv2.bilateralFilter(img,d,sigmaColor,sigmaSpace) 
		canny_img = cv2.Canny(blurred_img,50,150)
		cv2.imshow('Blurred Image',blurred_img)
		cv2.waitKey(1)
		cv2.imshow('Blur effect in Canny',canny_img)
		cv2.waitKey(1)
		ans = input("Try again?[y/n]")
		if (ans=='n'):
			return

def Gamma():
	print("check source code for implementation")
	while(True):
		gamma = float(input('Enter gamma value:'))
		gamma_img = np.power(img,gamma)
		canny_img = cv2.Canny(gamma_img,50,150)
		cv2.imshow('Gamma Image',gamma_img)
		cv2.waitKey(1)
		cv2.imshow('Gamma effect in Canny',canny_img)
		cv2.waitKey(1)
		ans = input("Try again?[y/n]")
		if (ans=='n'):
			return

while(True):
	os.system('cls||clear')
	print('1. Average')
	print('2. GaussianBlur')
	print('3. MedianBlur')
	print('4. BilateralFilter')
	print('5. Gamma')
	print('Any other key to exit')
	i = input('Choose any of the above: ')
	if i=='1':
		Average()
	elif i=='2':
		Gaussian()
	elif i=='3':
		MedianBlur()
	elif i=='4':
		BilateralFilter()
	elif i=='5':
		Gamma()
	else:
		exit()
	cv2.destroyAllWindows()