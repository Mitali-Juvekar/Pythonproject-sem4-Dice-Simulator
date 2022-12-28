#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[6]:


repeat = True
while repeat:
    print(random.randint(1,6))
    a = input("Do you want to roll again? :(y/n)")
    if a.lower() == "y":
        continue
    else:
        break


# In[21]:


from tkinter import *


# In[38]:


window=Tk()

lbl=Label(window, fg='red', font=("times", 260))

def dice_roll():
    n = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    lbl.config(text=f'{random.choice(n)}')
    lbl.pack()
    
btn=Button(window, text="Roll", fg='black', command = dice_roll)
btn.place(x=270, y=0)

# lbl=Label(window, text="This is Label widget", fg='red', font=("Helvetica", 16))
# lbl.place(x=60, y=50)

window.title('Dice Simulator')
window.geometry("600x500+10+20")
window.mainloop()


# In[ ]:




