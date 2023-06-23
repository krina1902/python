file=open("19filemanage.txt","w")
file.write("Welcome to the page of file manage...")
file.close()
print("File page working sucessfully....")
print("#"*70)

file=open("19filemanage.txt","r")
print(file.read())
file.close()
print("#"*70)

file=open("19filemanage.txt","a")
file.write("\nTry to something append on this page....")
file.close()
print("#"*70)
file=open("19filemanage.txt","r")
print(file.read())
file.close()
print("#"*70)


file=open("19filemanage.txt","w+")
file.write("W+ use for write and read")
print("where is cursor:",file.tell()) #tell use for find cursor
file.seek(0) #seek use for point the cursor
print(file.read())
file.close()
print("file executed.....")
print("#"*70)

file=open("19filemanage.txt","r+")
file.read()
file.write("\nr+ mode is use for first read and then write. for this mode first file is available or execute...")
file.seek(0)
print(file.read())
file.close()
print("#"*70)

