#!/usr/bin/env python
# coding: utf-8

# In[2]:


from linestickerdata import list_available
import matplotlib.pyplot as plt
available = list_available()
for row in available:
    if 'taste' in row:
        print(row['folder'], 'taste: ', row['taste'])
    if 'category' in row:
        print(row['folder'], 'category: ', row['category'])
    if 'character' in row:
        print(row['folder'], 'character: ', row['character'])


# In[3]:


import os


# In[5]:


path = "./alldata"
if os.path.isdir(path) == False:
    os.mkdir(path)


# In[9]:


from linestickerdata import get_image_paths
from skimage.io import imshow, imread,imsave
len(available)
i = 0
for row in available:
    if 'category' in row:
        print(row['folder'], 'category: ', row['category'],len(row['category']))
        for p in range(len(row['category'])):
            paths = get_image_paths(folder=row['folder'], character= row['category'][p], n=5, num_workers=1, seed=0)
            for im in range(len(paths)):
                rim = imread(paths[im])
                imsave(os.path.join(path,str(i)+str(p)+str(im)+".png"), rim)
                if im == 50:
                    print("ครึ่งทางละ")
    if 'taste' in row:
        print(row['folder'], 'taste: ', row['taste'],len(row['taste']))
        for p in range(len(row['taste'])):
            paths = get_image_paths(folder=row['folder'], character= row['taste'][p], n=5, num_workers=1, seed=0)
            for im in range(len(paths)):
                rim = imread(paths[im])
                imsave(os.path.join(path,str(i)+str(p)+str(im)+".png"), rim)
                if im == 50:
                    print("ครึ่งทางละ")
    if 'character' in row:
        print(row['folder'], 'character: ', row['character'],len(row['character']))
        for p in range(len(row['character'])):
            paths = get_image_paths(folder=row['folder'], character= row['character'][p], n=5, num_workers=1, seed=0)
            for im in range(len(paths)):
                rim = imread(paths[im])
                imsave(os.path.join(path,str(i)+str(p)+str(im)+".png"), rim)
                if im == 50:
                    print("ครึ่งทางละ")
    i = i+1
    print("save เสร็จหมดละ")            
                     
        
            


# In[ ]:




