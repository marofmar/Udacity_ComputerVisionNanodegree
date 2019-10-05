# -*- coding: utf-8 -*-
"""CVND_L4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_36_3C9qQCV7btlmxNogs81fNsTJvNOf

# Grid Image
"""

import numpy as np 
import matplotlib.image as mpimg 
import matplotlib.pyplot as plt 
import cv2

image = mpimg.imread('tigre.jpg') 
print('Image dimensions: ', image.shape)

gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) # change from color to greyscale 
plt.imshow(gray_image, cmap = 'gray') 

x = 400 
y = 300 
print(gray_image[y, x])

max_val = np.amax(gray_image) 
min_val = np.amin(gray_image) 
print('Max: ', max_val) 
print('Min: ', min_val)

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

"""# RGB split"""

rgb_image = mpimg.imread('tigre.jpg')
plt.imshow(image)

r = rgb_image[:, :, 0]
g = rgb_image[:, :, 1]
b = rgb_image[:, :, 2] 

#visualize individual color channel 
f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize = (20,10)) 
ax1.set_title('R channel') 
ax1.imshow(r, cmap = 'gray') 
ax2.set_title('G channel') 
ax2.imshow(g, cmap = 'gray') 
ax3.set_title('B channel') 
ax3.imshow(b, cmap = 'gray')



"""# Coding a Blue Screen"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt 
import numpy as np 
import cv2
# %matplotlib inline

pizza = cv2.imread('pizza_bluescreen.jpg')
print("This image is: ", type(image), ' with dimensions: ', image.shape)

plt.imshow(pizza) # opencv read in not RGB way but BGR way

image_copy = np.copy(pizza) # it is always safe to copy one 
image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB) 
plt.imshow(image_copy)



"""# Let's make the pizza float in galaxy!
## Color threshold, blue screen
"""

# define the color threshold (in this case, blue background) 
lower_blue = np.array([0,0,220])
upper_blue = np.array([50,50,255])

# define the masked area 
mask = cv2.inRange(image_copy, lower_blue, upper_blue) 
# visualiza the mask 
plt.imshow(mask, cmap = 'gray')

masked_image = np.copy(image_copy) 
masked_image[mask != 0] = [0,0,0]
plt.imshow(masked_image)

wid, height = image_copy.shape[:2]
print(wid, height)

background_image = cv2.imread('galaxy.jpg') 
background_image = cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB) 
crop_background = background_image[0:514, 0:816]
crop_background[mask==0] = [0,0,0]
plt.imshow(crop_background)

new = masked_image + crop_background
plt.imshow(new)



"""# HSV Color Space, Balloons"""

import numpy as np 
import matplotlib.pyplot as plt 
import cv2

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline 
ball = cv2.imread('tigre.jpg') 
plt.imshow(ball)

# change color to RGB (from BGR) 
tongue = cv2.cvtColor(ball, cv2.COLOR_BGR2RGB) 
plt.imshow(tongue)

r = tongue[:,:,0]
g = tongue[:,:,1]
b = tongue[:,:,2]

f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize = (20,10)) 

ax1.set_title('Red')
ax1.imshow(r, cmap = 'gray')

ax2.set_title('Green')
ax2.imshow(g, cmap = 'gray')

ax3.set_title('Blue')
ax3.imshow(g, cmap ='gray')

# convert from RGB to HSV 
hsv = cv2.cvtColor(tongue, cv2.COLOR_RGB2HSV)

h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]

f, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize = (20,10)) 

ax1.set_title('Hue')
ax1.imshow(h, cmap = 'gray') 

ax2.set_title('Saturation') 
ax2.imshow(s, cmap = 'gray') 

ax3.set_title('Value') 
ax3.imshow(v, cmap = 'gray')

# define our color selection criteria in RGB value 
lower_pink = np.array([180,0,100])
upper_pink = np.array([255,255,230])

# mask the image
mask_rgb = cv2.inRange(tongue, lower_pink, upper_pink) 
masked_image = np.copy(tongue) 
masked_image[mask_rgb==0] = [0,0,0]

plt.imshow(masked_image)

lower_hue = np.array([160,0,0])
upper_hue = np.array([180, 255,255])

# try HSV
mask_hsv = cv2.inRange(hsv, lower_hue, upper_hue)

masked_image = np.copy(tongue) 
masked_image[mask_hsv==0] = [0,0,0]

plt.imshow(masked_image)

