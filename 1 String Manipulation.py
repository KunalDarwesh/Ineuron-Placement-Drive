# -*- coding: utf-8 -*-
"""
@author: kunal.darwesh
"""
print("1. Want to see Original content \n2. Want to see Replaced file content \n")
ch=input("Enter you choice:")


def original_file_content():
  myBat = open(r'C:\Users\kunal.darwesh\Desktop\example.txt','w+')
  str1="This is a placement assignment"
  myBat.write(str1)
  myBat.close()
  
def replaced_file_content():
    myBat = open(r'C:\Users\kunal.darwesh\Desktop\example.txt','w+')
    str1="This is a placement assignment"
    str2=str1.replace("placement","screening")
    myBat.write(str2)
    print(str2)
    myBat.close()
  
if ch== "1":
    original_file_content()
else :
    replaced_file_content()