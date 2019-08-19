import io
#Thats the way to import all the stuff that the library have.

file = open("test_file.txt","w")

input_text = input()

file.write(input_text)
file.close()

