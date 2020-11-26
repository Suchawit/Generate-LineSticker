#!/usr/bin/env python
# coding: utf-8

# In[12]:


get_ipython().system('pip install --user linestickerdata==0.0.12')


# ### List all available sticker

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


# In[4]:


get_ipython().system('ls')


# In[5]:


path = "../non/pytorch-CycleGAN-and-pix2pix/alldata"
if os.path.isdir(path) == False:
    os.mkdir(path)


# In[6]:


os.path.join(path,str(1))


# ## List each path length

# In[9]:


from linestickerdata import get_image_paths
from skimage.io import imshow, imread,imsave
len(available)
for row in available:
    if 'taste' in row:
        for p in range(len(row['taste'])):
            paths = get_image_paths(folder=row['folder'], character= row['taste'][p], n=5, num_workers=1, seed=0)
            print(row['folder'], 'taste: ', row['taste'][p],len(paths))
    if 'category' in row:
        for p in range(len(row['category'])):
            paths = get_image_paths(folder=row['folder'], character= row['category'][p], n=5, num_workers=1, seed=0)
            print(row['folder'], 'category: ', row['category'][p],len(paths))
    if 'character' in row:
        for p in range(len(row['character'])):
            paths = get_image_paths(folder=row['folder'], character= row['character'][p], n=5, num_workers=1, seed=0)     
            print(row['folder'], 'character: ', row['character'][p],len(paths))


# ## Save image to path directory

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
                     
        
            


# In[2]:


from linestickerdata import get_image_paths
paths = get_image_paths(folder="data", character="Female Characters", n=5, num_workers=1, seed=0)
paths = get_image_paths(folder="data", taste="Polite Language",n=5, num_workers=1, seed=0)
paths = get_image_paths(folder="dataofficial", category="Big stickers", n=5, num_workers=1, seed=0)
paths = get_image_paths(folder="dataofficial-th", category="มาสคอต", n=5, num_workers=1, seed=0)
paths = get_image_paths(folder="data-th", taste="ตลก", n=5, num_workers=1, seed=0)
paths = get_image_paths(folder="data-th", character="หมี", n=5, num_workers=1, seed=0)


# In[13]:


import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imshow, imread
from linestickerdata import get_image_paths
paths = get_image_paths(folder="data-th", character="อาหาร", n=5, num_workers=1, seed=0)
width=5
height=5
rows = 4
cols = 4
axes=[]
fig=plt.figure()

for a in range(rows*cols):
    im = imread(paths[a])
    axes.append( fig.add_subplot(rows, cols, a+1) )
    subplot_title=("Stickers"+str(a+1))
    axes[-1].set_title(subplot_title)  
    plt.imshow(im)
fig
plt.show()


# In[ ]:




