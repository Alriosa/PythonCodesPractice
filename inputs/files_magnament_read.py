import io

file=open("test_file.txt","r") #this time "r" stands for read

stored_lines = file.readlines() #here in this var we will store the lines

file.close()

print(stored_lines[0]) #print the linea number 0