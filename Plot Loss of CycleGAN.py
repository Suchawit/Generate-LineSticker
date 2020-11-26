#!/usr/bin/env python
# coding: utf-8

# In[50]:


import numpy as np
num_lines = sum(1 for line in open('../non/pytorch-CycleGAN-and-pix2pix/checkpoints/maps_cropsticker2face/loss_log.txt'))
D_A = np.zeros(num_lines-1)
G_A = np.zeros(num_lines-1)
D_B = np.zeros(num_lines-1)
G_B = np.zeros(num_lines-1)

f = open('../non/pytorch-CycleGAN-and-pix2pix/checkpoints/maps_cropsticker2face/loss_log.txt','r')

print(f.readline())
for i in range(num_lines-1):
    text = f.readline()
    sptext = text.split(')')
    spsptext = sptext[1].split(' ')
    last_itr_of_ep = sptext[0].split(' ')[3]
    last_itr_of_ep = last_itr_of_ep.replace(',', '')
    last_itr_of_ep = int(last_itr_of_ep)
    if last_itr_of_ep >= 600:
        D_A[i]= spsptext[2]
        G_A[i]= spsptext[4]
        D_B[i]= spsptext[10]
        G_B[i]= spsptext[12]


# In[61]:


import matplotlib.pyplot as plt
D_A = [i for i in D_A if i != 0]
G_A = [i for i in G_A if i != 0]
D_B = [i for i in D_B if i != 0]
G_B = [i for i in G_B if i != 0]


# In[62]:


plt.plot(D_A)
plt.ylabel('Discriminator A')
plt.show()


# In[63]:


plt.plot(G_A)
plt.ylabel('Generator A')
plt.show()


# In[64]:


plt.plot(D_B)
plt.ylabel('Discriminator B')
plt.show()


# In[65]:


plt.plot(G_B)
plt.ylabel('Generator B')
plt.show()

