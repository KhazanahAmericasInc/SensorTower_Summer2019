#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:25:30 2019

@author: clair
"""


"""Preprocessing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/Blaizzy/BiSeNet-Implementation/blob/master/Preprocessing.ipynb

# **Image preprocessing**
**Image processing** is divided into analogue image processing and digital image processing.

**Digital image processing** is the use of computer algorithms to perform image processing on digital images. It allows a much wider range of algorithms to be applied to the input data - the aim of digital image processing is to improve the image data (features) by suppressing unwanted distortions and/or enhancement of some important image features so that our **AI models** can benefit from this improved data to work on.

"""


import os
import numpy as np
import matplotlib.pyplot as plt
import cv2

raw_image_path = "./raw_image"
resized_image_path = "./resized_image"

def loadImages(path):
    '''Put files into lists and return them as one list with all images 
     in the folder'''
    image_files = sorted([os.path.join(path, file)
                          for file in os.listdir(path)
                          if file.endswith('.png') or file.endswith('.jpg') or file.endswith('jpeg')])
    return image_files

"""# **Displaying Images**"""

# Display two images
def display(a, b, title1 = "Original", title2 = "Edited"):
    plt.subplot(121), plt.imshow(a), plt.title(title1)
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(b), plt.title(title2)
    plt.xticks([]), plt.yticks([])
    plt.show()

# Display one image
def display_one(a, title1 = "Original"):
    plt.imshow(a), plt.title(title1)
    plt.show()


def make_dir(path):
    try:
        os.makedirs(path)
    except:
        pass


"""# Preprocessing the images:
* Read image
* Resize image 
* Remove noise(Denoise)
* Segmentation
* Morphology(smoothing edges)
"""

# Preprocessing
def processing(data, subdir):
    # Reading all images to work
    img = [cv2.imread(i, cv2.IMREAD_UNCHANGED) for i in data]
    try:
        print('Original size',img[0].shape)
    except AttributeError:
        print("shape not found")
   
    # --------------------------------
    # setting dim of the resize
    height = 64
    width = 64
    dim = (width, height)
    res_img = []
    for i in range(len(img)):
        res = cv2.resize(img[i], dim, interpolation=cv2.INTER_LINEAR)
        res_img.append(res)
        
    c = 0
    print(len(res_img))
    
    print(os.path.join(resized_image_path, subdir))
    make_dir(os.path.join(resized_image_path, subdir))
    
    for i in res_img:
        newimg_name = os.path.join(resized_image_path, subdir, "timbertruck" + str(c) + ".jpg")

        c += 1
        cv2.imwrite(newimg_name, i)
    
        
    # Checcking the size
    try:
        print('RESIZED', res_img[1].shape)
    except AttributeError:
        print("shape not found")
    
    
    # Visualizing one of the images in the array
    original = res_img[1]
    display_one(original)
#    # ----------------------------------
#    # Remove noise
#    # Using Gaussian Blur
#    no_noise = []
#    for i in range(len(res_img)):
#        blur = cv2.GaussianBlur(res_img[i], (5, 5), 0)
#        no_noise.append(blur)
#
#
#    image = no_noise[1]
#    display(original, image, 'Original', 'Blured')
#     #---------------------------------
#     # Segmentation
#     gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
#     ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

#     # Displaying segmented images
#     display(original, thresh, 'Original', 'Segmented')
#     # Further noise removal (Morphology)
#     kernel = np.ones((3, 3), np.uint8)
#     opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

#     # sure background area
#     sure_bg = cv2.dilate(opening, kernel, iterations=3)

#     # Finding sure foreground area
#     dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
#     ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

#     # Finding unknown region
#     sure_fg = np.uint8(sure_fg)
#     unknown = cv2.subtract(sure_bg, sure_fg)

#     #Displaying segmented back ground
#     display(original, sure_bg, 'Original', 'Segmented Background')

#     # Marker labelling
#     ret, markers = cv2.connectedComponents(sure_fg)

#     # Add one to all labels so that sure background is not 0, but 1
#     markers = markers + 1

#     # Now, mark the region of unknown with zero
#     markers[unknown == 255] = 0

#     markers = cv2.watershed(image, markers)
#     image[markers == -1] = [255, 0, 0]

#     # Displaying markers on the image
#     display(original, markers, 'Original', 'Marked')




"""# Main Function the heart of the program"""

def main():
    # calling global variable
    global image_path
    '''The var Dataset is a list with all images in the folder '''
    for i in os.listdir(raw_image_path):
        image_path = os.path.join(raw_image_path, i)
        
        try:
            dataset = loadImages(image_path)
        except:
            print("error message")
        
        print("List of files the first 3 in the folder:\n",dataset[:3])
        print("--------------------------------")
        
        # sending all the images to pre-processing
        processing(dataset, i)
   

  
main()