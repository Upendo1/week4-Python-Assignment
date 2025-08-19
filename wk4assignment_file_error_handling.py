#1.File Read & Write Challenge : Create a program that reads a file and writes a modified version to a new file.
# Question 1: File Read & Write Challenge

# Open the original file for reading
#Creating a file for reading
file = open ("input.txt","w")
file.write ("Input file")
file.close()

#Reading a file
file = open("input.txt", "r")  
content = file.read()
file.close()

# Modify the content (convert to uppercase)
modified_content = content.upper()

# Write modified content to a new file
file = open("output.txt", "w")
file.write(modified_content)
file.close()

print("Success! Modified file has been written to 'output.txt'.")

#2.Error Handling Lab : Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
filename = input("Enter the name of the file to read: ")

try:
    # Try to open and read the file
    file = open(filename, "r")
    content = file.read()
    file.close()

    print("File read successfully! Here is the content:")
    print(content)  # <-- Must be indented properly inside try

except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except IOError:
    print(f"Error: Cannot read the file '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")