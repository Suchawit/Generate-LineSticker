#!/usr/bin/env python
# coding: utf-8

# In[52]:


import face_recognition


# In[14]:


from linestickerdata import get_image_paths
from skimage.io import imshow, imread,imsave


# In[3]:


paths = get_image_paths(folder="data", character="Female Characters", n=5, num_workers=1, seed=0)


# In[61]:


image = face_recognition.load_image_file(paths[0])
face_locations = face_recognition.face_locations(image)


# In[18]:


imshow(image)


# # Crop image

# In[36]:


ii=image[face_locations[0][0]:face_locations[0][2],face_locations[0][3]:face_locations[0][1]]


# In[37]:


imshow(ii)


# In[26]:


face_locations[0]


# In[67]:


image = face_recognition.load_image_file(paths[99])


# In[68]:


imshow(image)


# In[69]:


face_locations = face_recognition.face_locations(image)


# In[70]:


face_locations


# In[25]:


i = imread("../../non/pytorch-CycleGAN-and-pix2pix/sticker2sketch/trainA/01.png")


# In[26]:


imshow(i)


# In[13]:


import json
import os
from linestickerdata import get_image_paths
from skimage.io import imshow, imread,imsave
import face_recognition


# In[2]:


f = open('../../non/pytorch-CycleGAN-and-pix2pix/output.json')


# In[3]:


data = json.load(f)


# In[4]:



len(list(data)), list(data)


# In[5]:


data


# In[15]:



path = "../../non/pytorch-CycleGAN-and-pix2pix/adata"
dictpath = "../pytorch-CycleGAN-and-pix2pix/adata"
pic = "01979.png"
fullpath  = os.path.join(path,pic)
fulldictpath = os.path.join(dictpath,pic)
i = imread(fullpath)
print(fullpath)
print(fulldictpath)
imshow(i)


# In[16]:


if data[fulldictpath]:
    print("List is not empty")
data[fulldictpath]


# #### data type is dict -> list -> dict -> list then convert float into int

# In[17]:


ii=i[int(data[fulldictpath][0]['bbox'][1]):int(data[fulldictpath][0]['bbox'][3]),int(data[fulldictpath][0]['bbox'][0]):int(data[fulldictpath][0]['bbox'][2])]


# In[18]:


k = fullpath.split('/')


# In[19]:


k[-1]


# In[20]:


image = face_recognition.load_image_file(fullpath)
face_locations = face_recognition.face_locations(image)
print(face_locations)
if not face_locations:
    print("ไม่ใช่หน้าคน")
    imshow(ii)
else:
    print("หน้าคน")
    imshow(ii)
ii=image[int(data[fulldictpath][0]['bbox'][1]):int(data[fulldictpath][0]['bbox'][3]),int(data[fulldictpath][0]['bbox'][0]):int(data[fulldictpath][0]['bbox'][2])]        
        


# In[22]:


import os
path = "../../non/pytorch-CycleGAN-and-pix2pix/adata"
pathsave = "../../non/pytorch-CycleGAN-and-pix2pix/cropfacesticker"
if os.path.isdir(pathsave) == False:
    os.mkdir(pathsave)
for row in list(data):
    if data[row]:
        piclo = row.split('/')
        print("Doing this image "+piclo[-1])
        fullpath  = os.path.join(path,piclo[-1])
        image = face_recognition.load_image_file(fullpath)
        face_locations = face_recognition.face_locations(image)
        if not face_locations:
            print("saving")
            cimage=image[int(data[row][0]['bbox'][1]):int(data[row][0]['bbox'][3]),int(data[row][0]['bbox'][0]):int(data[row][0]['bbox'][2])]
            imsave(os.path.join(pathsave,piclo[-1]), cimage)


# In[32]:


import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imshow, imread
from linestickerdata import get_image_paths
filelist=os.listdir(pathsave)
width=5
height=5
rows = 4
cols = 4
axes=[]
fig=plt.figure()

for a in range(rows*cols):
    fullpaths  = os.path.join(pathsave,os.listdir(pathsave)[a])
    im = imread(fullpaths)
    axes.append( fig.add_subplot(rows, cols, a+1) )
    subplot_title=("Stickers"+str(a+1))
    axes[-1].set_title(subplot_title)  
    plt.imshow(im)
fig
plt.show()


# In[ ]:




