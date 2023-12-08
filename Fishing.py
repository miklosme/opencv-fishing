#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pipenv install opencv-python')


# In[32]:


get_ipython().system('pipenv install pyautogui')


# In[40]:


import cv2
import numpy as np
import pyautogui


# In[41]:


water_img = cv2.imread('water.png', cv2.IMREAD_UNCHANGED)
lure_img = cv2.imread('lure.png', cv2.IMREAD_UNCHANGED)
catch_img = cv2.imread('catch.png', cv2.IMREAD_UNCHANGED)


# In[51]:


cv2.imshow('Water', water_img)
cv2.waitKey()
cv2.destroyAllWindows()


# In[52]:


# result = cv2.matchTemplate(water_img, catch_img, cv2.TM_CCOEFF_NORMED)
result = cv2.matchTemplate(water_img, lure_img, cv2.TM_SQDIFF_NORMED)


# In[53]:


# cv2.imshow('Result', result)
# cv2.waitKey()
# cv2.destroyAllWindows()


# In[54]:


minv, maxv, minl, maxl = cv2.minMaxLoc(result)


# In[55]:


# maxl


# In[56]:


# w = lure_img.shape[1]
# h = lure_img.shape[0]


# In[57]:


# cv2.rectangle(water_img, maxl, (maxl[0] + w, maxl[1] + h), (0,255,255), 2)


# In[58]:


# pyautogui.position()


# In[59]:


pyautogui.moveTo(x=maxl[0], y=maxl[1], duration=0.7)


# In[ ]:




