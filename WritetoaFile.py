filename = "sample.txt"

# Take input from user
text = input("Enter text to write into file: ")

# Write to file
file = open(filename, "w")
file.write(text)
file.close()

print("Data written to file successfully.")

# Ask user if they want to open the file
choice = input("Do you want to open the file? (yes/no): ")

if choice.lower() == "yes":
    file = open(filename, "r")
    content = file.read()
    file.close()

    print("\nFile Content:\n")
    print(content)
else:
    print("File not opened.")


