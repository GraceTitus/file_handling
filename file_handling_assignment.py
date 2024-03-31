"""File Handling Assignment
Demonstrate your understanding of Python file handling by completing the following tasks.
Tasks:
1)File Creation:
-Create a Python script (file_handling_assignment.py) that does the following:
-Creates a new text file named "my_file.txt" in write mode ('w').
-Write at least three lines of text to the file, including a mix of strings and numbers.
2)File Reading and Display:
-Enhance your script to read the contents of "my_file.txt" and display them on the console.
3)File Appending:
-Modify the script to open "my_file.txt" in append mode ('a').
-Append three additional lines of text to the existing content.
4)Error Handling:
-Implement error handling using try, except, and finally blocks to manage potential file-related exceptions (e.g., FileNotFoundError, PermissionError).
"""
# Open "my_file.txt" in write mode ('w')
with open("my_file.txt", "w") as file:
    # Write three lines of text to the file
    file.write("This is line 1.\n")
    file.write("12345\n")
    file.write("Another line of text.")


    # Open the file in read mode
with open("my_file.txt", "r") as file:
    # Read the contents of the file
    file_content = file.read()
    # Display the contents on the console
    print("Contents of my_file.txt:")
    print(file_content)

# Open the file in append mode ('a')
try:
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text
        file.write("\nAdditional line 1\n")
        file.write("Additional line 2\n")
        file.write("Additional line 3\n")
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to open the file.")
finally:
    print("File appending operation completed.")

# 4) Error Handling
# Implement error handling using try, except, and finally blocks to manage potential file-related exceptions
try:
    # Perform file-related operations here
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print("Contents of my_file.txt:")
        print(contents)
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied to open the file.")
finally:
    print("Error handling completed.")
