import io
#Thats the way to import all the stuff that the library have.

file = open("test_file.txt","w") #The "w" stands for "write" that means i will open the file in mode writeable

input_text = input()

file.write(input_text)
file.close()

