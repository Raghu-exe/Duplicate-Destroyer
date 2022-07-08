import tkinter as tk
from tkinter import *




def submit(): ## Taking in user information
    
    ## userNameVar.set("")
    string1 =  str(userNameVar.get())
    
    ## destinationVar.set("")
    string2 = str(destinationVar.get())
    
    ## folderNameVar.set("")
    string3 = str(folderNameVar.get())
    
    root.quit()

    
    return [string1, string2, string3]




# creating a root window
root = Tk()


root.geometry('575x300')
root.title("DuplicateDestroyer - Raghu Wable")


## global userNameVar
userNameVar = StringVar()

## global destinationVar 
destinationVar = StringVar()

## global folderNameVar
folderNameVar = StringVar()
    
greeting = tk.Label(root, text= "DO NOT PUT ANY UNINTENDED SPACES IN YOUR RESPONSES!" + '\n' + "Make a copy of the files in case of mistype").place(x = 120, y = 10) 

## Enter User's system name
userName = tk.Label(root, text= "Enter your PC user Name (Case Senstive): ").place(x = 10,y = 50)  
userNameEntry = tk.Entry(root, bd = 2, font = "Nova_Proxima", textvariable = userNameVar).place(x = 325, y = 50)  


 

## Enter User's file destination name
destinationName = tk.Label(root, text= "Enter your file destination/Location on PC (Case Senstive): ").place(x = 10,y = 100)  
destinationEntry = tk.Entry(root, bd = 2, font = "Nova_Proxima", textvariable = destinationVar).place(x = 325, y = 100)



## Enter User's folder name  
folderName = tk.Label(root, text= "Enter your Folder Name (Case Senstive): ").place(x = 10,y = 150)  
folderNameEntry = tk.Entry(root, bd = 2, font = "Nova_Proxima", textvariable = folderNameVar).place(x = 325, y = 150) 





submit_btn = tk.Button(root,text = 'Submit', command = submit, width = 10).place(x = 250, y = 210)





root.mainloop()





