# EXERCISE 7 - CLEAR THE CLUTTER
# Problem Statement: Write a program to clear the clutter inside a folder on your computer. You should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder. Do the same for other file formats.



import os

files = os.listdir("ClutteredFolder")

i = 1
for file in files:
    if ".png" in file:      # if file.endswith(".png"):
        os.rename(f"ClutteredFolder/{file}", f"ClutteredFolder/{i}.png")
        i = i + 1

j = 1
for file in files:
    if ".pdf" in file:      # if file.endswith(".pdf"):
        os.rename(f"ClutteredFolder/{file}", f"ClutteredFolder/{j}.pdf")
        j = j + 1

k = 1
for file in files:
    if ".txt" in file:      # if file.endswith(".txt"):
        os.rename(f"ClutteredFolder/{file}", f"ClutteredFolder/{k}.txt")
        k = k + 1