# file_path = 'youtube.txt'  # File ka path

# # Open file in write mode
# with open(file_path, 'w') as file:
#     file.write("Hello, this is a test file.\n")
#     file.write("Python is awesome!\n")

# print("Data has been written to the file.")

file=open('youtube.txt','r')
print(file.read())
# file.write("Hello, this is a test file.\n")
file.close()

# Step 1: Nayi file create karna aur write mode mein likhna
with open('newfile.txt', 'w') as file:
    file.write("This is the first line of the new file.\n")
    file.write("Python makes file handling easy.\n")

print("File created and data written successfully.")

# Step 2: File ko read karna
with open('newfile.txt', 'r') as file:
    content = file.read()

print("\nContent of the file:")
print(content)
