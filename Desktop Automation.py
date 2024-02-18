#!/usr/bin/env python
# coding: utf-8

# In[94]:


import os, shutil


# In[95]:


path = r"C:\Users\chand\OneDrive\Desktop/" #Replace the Path with the path you want ur file automation to happen.


# In[96]:


file_name = os.listdir(path) 


# In[97]:


folder_names = ['Image files', 'Misc', 'exe files'] #Create the names of files: Acrodding to Type of File format, for eg: PDF files for 'pdf' files or Use your choice of name 

for loop in range(0,3): #If you're using/created multiple file folders above, Add up how many number of folders you created and change the '3'to the number accordingly.
    if not os.path.exists(path + folder_names[loop]):
        #print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])


# In[98]:


for file in file_name:
    if ".png" in file and not os.path.exists(path + "Image files/" + file): #Type of 'File' type replace 'png'
        shutil.move(path + file, path + "Image files/" + file)
    elif ".txt" in file and not os.path.exists(path + "Misc/" + file):
                shutil.move(path + file, path + "Misc/" + file)
    elif ".jpg" in file and not os.path.exists(path + "exe files/" + file):
                shutil.move(path + file, path + "exe files/" + file)
    
            
        


# In[ ]:




