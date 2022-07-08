import os
from tkinter import *
import GUI_entry



## finding the directory the user wants to examine for duplicate files. 


def pathName (userName, destination, folderName):
   
   return "C:\\Users\\" + userName + "\\" + destination + "\\" + folderName

pathList = GUI_entry.submit()
         
path = pathName(pathList[0], pathList[1], pathList[2]) ## assigning the path specified by the user



keyList = []

mainValueList = []
dictionary = {}

iterateFile = None
fileSize = None
fileType = None
mainCase = None

def createDictionary(dicts, keys, values):
   
   
   for i in range(len(keys)):
      dicts[keys[i]] = values[i]
      
   return dicts



for filename in os.listdir(path):
    f = os.path.join(path,filename)

    if os.path.isfile(f):  
      iterateFile = filename
      keyList.append(iterateFile) ## making a list of all the files in the directory

      fileSize = os.path.getsize(f) ## getting the size of the file 
      
      fileTypeList = os.path.splitext(iterateFile) ## getting the type of the file   
      fileType = fileTypeList[1]
      
      individualValueList = [] ## creating a temp list that holds the individual information for each file
      
      individualValueList.append(fileSize) ## appending the file information into the temp list
      individualValueList.append(fileType)
      
      mainValueList.append(individualValueList) ## appending the temp list to the permanent value list to make a 2d list


dictionary = createDictionary(dictionary, keyList, mainValueList)     

root = Tk()
root.geometry('500x500')
root.title("DuplicateDestroyer - Raghu Wable")


    
text = Text(root, width=80, height=15)

text.pack()

for n in keyList:

    text.insert(END, n + '\n')
##text.pack()


submit_btn = Button(root, text = 'Submit', command = root.destroy, width = 10)
submit_btn.pack(side=BOTTOM)

Exit_btn = Button(root, text = 'Exit Program', command = exit, width = 10)
Exit_btn.pack(side=BOTTOM)

message = Label(root, wraplength= 500,text= "These are the listed files inside the given directory." + '\n' + "If incorrect folder -> click EXIT PROGRAM and restart!. ", font=("Arial", 15)).place(x= 25, y = 350)  

root.mainloop()

   
## file deletion part starts here

for aFile in os.listdir(path):
   fpath = os.path.join(path, aFile)
      ## print(fpath)
   if os.path.isfile(fpath):  
      
      fSize = os.path.getsize(fpath) ## getting the size of the file 
            
      fTypeList = os.path.splitext(aFile) ## getting the type of the file   
      fType = fTypeList[1]
            
      singularValueList = [] ## creating a temp list that holds the individual information for each file
            
      singularValueList.append(fSize) ## appending the file information into the temp list
      singularValueList.append(fType)
         ## print(singularValueList)
         
      counter = 0  
         
      for f in dictionary.values():
            
         if singularValueList == f:
               
            counter = counter + 1
               
            while counter > 1:
                  
               os.remove(fpath)
               counter = 0
                  




## printing remaining files part
remainingkeyList = []

      
for filename in os.listdir(path):
    f = os.path.join(path,filename)

    if os.path.isfile(f):  
      iteratedFile = filename
      remainingkeyList.append(iteratedFile) ## making a list of all the files in the directory
     

root = Tk()
root.geometry('500x500')
root.title("DuplicateDestroyer - Raghu Wable")


    
text = Text(root, width=80, height=15)

text.pack()

for n in remainingkeyList:

    text.insert(END, n + '\n')
##text.pack()



submit_btn = Button(root, text = 'DONE', command = root.destroy, width = 10)
submit_btn.pack(side=BOTTOM)

message = Label(root, wraplength= 500,text= "Success!." + '\n' + "Here are the remaining files in your PC folder. ", font=("Arial", 15)).place(x= 25, y = 350)  

root.mainloop()





